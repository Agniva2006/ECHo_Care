import os
import requests
from dotenv import load_dotenv

from utils.prompts import ECHOCARE_PROMPT
from utils.memory import EchoMemory
from utils.deep_emotion import deep_emotion_detect
from utils.comfort import comfort_phrases
from utils.cbt import cbt_reframe
from utils.personality import detect_user_style, adapt_prompt_for_style

load_dotenv()

USER_ID = os.getenv("USER_ID", "default_user")
memory = EchoMemory(user_id=USER_ID, max_items=50)

OLLAMA_HOST = os.getenv("OLLAMA_HOST", "http://localhost:11434")
OLLAMA_MODEL = os.getenv("OLLAMA_MODEL", "llama3.1:8b")

# ---------------------------
# Crisis detection & response
# ---------------------------
CRISIS_PHRASES = [
    "i don't want to live", "i dont want to live", "i want to die", "end my life",
    "kill myself", "i can't do this anymore", "i cant do this anymore", "i can't take it",
    "i cant take it", "i want this to end", "i want it to stop", "i don't want to be here",
    "i dont want to be here", "disappear", "i'm scared of myself", "scared of what i might do",
    "leap like this", "end everything", "i want to end", "i'm going to end it"
]

def is_crisis(text: str) -> bool:
    if not text:
        return False
    t = text.lower()
    return any(phrase in t for phrase in CRISIS_PHRASES)

CRISIS_RESPONSE = """
I'm really glad you told me this — it takes real courage to share something so heavy.
You don't have to face this alone. Your safety matters and I want you to be safe right now.

Are you in a safe place at this moment?

If you can, please consider reaching out to someone you trust or your local emergency services.
If you feel like you might act on these thoughts, please call your local emergency number or a crisis line right now.
I'm here with you in this moment.
"""

# ---------------------------
# Main generator
# ---------------------------
def generate_reply(user_text: str, max_tokens: int = 300, temperature: float = 0.65) -> str:

    # Highest priority: crisis override
    if is_crisis(user_text):
        return CRISIS_RESPONSE.strip()

    # Save to memory (persistent)
    memory.add(user_text)
    memory_context = memory.get_summary()

    # Deep emotion detection
    emotion, scores = deep_emotion_detect(user_text)
    comfort = comfort_phrases.get(emotion, "")

    # CBT safe hint
    cbt_hint = cbt_reframe(user_text)

    # Personality / style adaptation
    user_style = detect_user_style(memory.memories[-20:]) if hasattr(memory, "memories") else "neutral"

    # Build safe prompt (no assumptions, no intimate nicknames)
    base_prompt = f"""{ECHOCARE_PROMPT}

Detected Emotion: {emotion}
Comfort: {comfort}
CBT Hint: {cbt_hint}

Memory Context:
{memory_context}

User: {user_text}

Instructions for EchoCare:
- Respond with empathy, clarity, and realism.
- Do NOT assume facts that the user did not state.
- Avoid intimate or overly familiar nicknames (do not use 'sweetheart', 'darling', etc.).
- If the user expresses crisis, do not continue normal conversation — prioritize safety.
- Keep replies 3-6 sentences, supportive and grounding.
"""

    prompt = adapt_prompt_for_style(base_prompt, user_style)

    payload = {
        "model": OLLAMA_MODEL,
        "prompt": prompt,
        "temperature": temperature,
        "max_tokens": max_tokens,
        "stream": False
    }

    url = f"{OLLAMA_HOST}/api/generate"

    try:
        r = requests.post(url, json=payload, timeout=60)
        r.raise_for_status()
        data = r.json()

        if isinstance(data, dict):
            if "response" in data:
                return data["response"].strip()
            if "text" in data:
                return data["text"].strip()
            choices = data.get("choices")
            if choices and isinstance(choices, list):
                return choices[0].get("text", "").strip()

        return str(data).strip()
    except Exception as e:
        print("LLM call failed:", e)
        return ("I'm here for you — I had a small hiccup but I'm still listening. "
                "Could you tell me that again gently?")
