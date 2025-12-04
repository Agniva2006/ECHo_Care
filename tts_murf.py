# tts_murf.py — EchoCare Ultra-Premium TTS
# Supports Murf AI TTS with styles, cadence, and safe fallback handling

import os
import base64
import requests
from dotenv import load_dotenv

load_dotenv()

MURF_API_KEY = os.getenv("MURF_API_KEY")
MURF_URL = "https://api.murf.ai/v1/speech/generate"

# EchoCare voice library presets (you can change these based on Murf voice list)
VOICE_PRESETS = {
    "soft": "en-US-Angela",
    "warm": "en-US-Luna",
    "friend": "en-US-Kevin",
    "therapist": "en-US-Sierra",
    "asmr": "en-US-Michelle"
}

def _download_url_to_file(url: str, output_file: str):
    """Stream-download a URL to output_file."""
    try:
        with requests.get(url, stream=True, timeout=30) as r:
            r.raise_for_status()
            with open(output_file, "wb") as f:
                for chunk in r.iter_content(chunk_size=8192):
                    if chunk:
                        f.write(chunk)
        return output_file
    except Exception as e:
        raise RuntimeError(f"Failed downloading Murf audio from URL: {e}")


def murf_tts(
    text: str,
    output_file: str = "echocare_output.wav",
    voice: str = "soft",
    style: str = None,
    cadence: float = 1.0
):
    """
    Generate TTS audio using Murf AI.

    Args:
        text:         Input text to convert.
        output_file:  Saved WAV path.
        voice:        Voice preset name (soft/warm/friend/etc).
        style:        Optional Murf style ("Conversational", "Calm", etc).
        cadence:      Playback pacing multiplier (1.0 = normal).
    """

    if not MURF_API_KEY:
        raise RuntimeError("MURF_API_KEY missing in .env")

    # Pick voice from presets or fallback to Angela
    voice_id = VOICE_PRESETS.get(voice, "en-US-Angela")

    payload = {
        "voiceId": voice_id,
        "text": text,
        "format": "wav"
    }
    if style:
        payload["style"] = style

    # Debug logs
    print("\n=== Murf TTS Request ===")
    print("Voice:", voice_id)
    print("Cadence:", cadence)
    print("Applying style:", style)
    print("Payload keys:", list(payload.keys()))
    print("=========================\n")

    headers = {
        "accept": "application/json",
        "Content-Type": "application/json",
        "api-key": MURF_API_KEY
    }

    # -- SEND REQUEST --
    resp = requests.post(MURF_URL, json=payload, headers=headers, timeout=30)
    print("Status:", resp.status_code)
    print("Raw Murf Response (first 500 chars):\n", resp.text[:500], "\n")

    # If non-200, raise with full content
    if resp.status_code != 200:
        raise RuntimeError(f"Murf TTS error {resp.status_code}: {resp.text}")

    data = resp.json()

    # -----------------------------
    # CASE 1: Murf returned Base64
    # -----------------------------
    if data.get("audioData"):
        try:
            audio_bytes = base64.b64decode(data["audioData"])
            with open(output_file, "wb") as f:
                f.write(audio_bytes)
            print("Saved base64 audio to:", output_file)
            return output_file
        except Exception as e:
            raise RuntimeError(f"Failed decoding Base64 audio: {e}")

    # -----------------------------
    # CASE 2: Murf returned a URL
    # -----------------------------
    audio_url = (
        data.get("audioFile") or
        data.get("audioUrl") or
        data.get("audio_path")
    )

    if audio_url:
        print("Presigned URL detected — downloading:", audio_url)
        return _download_url_to_file(audio_url, output_file)

    # -----------------------------
    # CASE 3: No audio -> Fatal
    # -----------------------------
    raise RuntimeError("Murf returned no audioData or audioFile → " + resp.text)
