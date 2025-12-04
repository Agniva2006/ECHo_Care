# asr.py — EchoCare Ultra-Premium Speech-to-Text
# Uses Faster-Whisper for fast CPU transcription

from faster_whisper import WhisperModel

# Load model once at import
# "base" = good accuracy + fast enough for real-time on CPU
model = WhisperModel(
    model_size_or_path="base",
    device="cpu",
    compute_type="int8"     # fastest on CPU
)

def transcribe(path: str) -> str:
    """
    Transcribes an audio file to text using faster-whisper.
    Handles empty audio gracefully.
    """
    print(f"[ASR] Transcribing: {path}")

    text = ""
    try:
        segments, info = model.transcribe(path)

        for seg in segments:
            if hasattr(seg, "text") and seg.text.strip():
                text += seg.text.strip() + " "

        text = text.strip()

        if not text:
            print("[ASR] No speech detected.")
            return "..."

        print(f"[ASR] Transcription: {text}")
        return text

    except Exception as e:
        print("[ASR] Error:", e)
        return "Sorry, I couldn't hear that clearly. Could you say it again?"
