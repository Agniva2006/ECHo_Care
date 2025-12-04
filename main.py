import streamlit as st
from dotenv import load_dotenv
import os

from utils.audio import record_audio, play_audio
from asr import transcribe
from llm_agent import generate_reply
from tts_murf import murf_tts
from utils.emotion import detect_emotion
from utils.comfort import comfort_phrases

load_dotenv()

# --------------------------
# 🔹 Initialize session state
# --------------------------
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []   # full conversation history

if "last_emotion" not in st.session_state:
    st.session_state.last_emotion = "neutral"

# --------------------------
# 🔹 Streamlit UI
# --------------------------
st.set_page_config(page_title="EchoCare", page_icon="🎧")
st.title("🎧 EchoCare — Emotional Wellness Voice Companion")
st.write(
    "Speak for a few seconds, and EchoCare will respond with supportive "
    "guidance and a calming voice."
)

st.markdown("---")

col1, col2 = st.columns([1, 3])

with col1:
    duration = st.number_input("🎙️ Recording Duration (seconds)", 
                               min_value=2, max_value=12, value=6)

with col2:
    st.write("🤖 Current Model:", os.getenv("OLLAMA_MODEL", "llama3.1:8b"))

# --------------------------
# 🔹 Main Voice Interaction
# --------------------------

if st.button("🎤 Speak Now"):
    st.info("Listening...")
    
    audio_path = record_audio(duration=int(duration), filename="input.wav")
    st.success("Recorded ✔ — transcribing...")

    user_text = transcribe(audio_path)

    st.markdown(f"### 🗣️ You said:\n> {user_text}")

    # --------------------------
    # 🔹 Emotion Detection
    # --------------------------
    emotion = detect_emotion(user_text)
    st.session_state.last_emotion = emotion

    comfort_line = comfort_phrases.get(emotion, "")

    if emotion != "neutral":
        st.write(f"**❤️ Detected emotion:** `{emotion}`")
        st.write(f"**EchoCare comforting note:** {comfort_line}")

    # --------------------------
    # 🔹 Command-based modes
    # --------------------------
    cmd = user_text.lower().strip()

    # Grounding Mode
    if "ground me" in cmd or "i need grounding" in cmd or "dissociating" in cmd:
        reply = (
            "Let's take a grounding moment. Look around you and name:\n"
            "• 1 thing you can smell\n"
            "• 2 things you can touch\n"
            "• 3 things you can see\n"
            "Whenever you're ready, tell me the first one."
        )

    # Breathing Support
    elif "calm down" in cmd or "breathe" in cmd or "panic" in cmd:
        reply = (
            "Let’s do a gentle breathing exercise together.\n\n"
            "Inhale slowly for **4 seconds**…\n"
            "Hold for **2 seconds**…\n"
            "Exhale softly for **6 seconds**.\n\n"
            "Tell me how your body feels now."
        )

    else:
        st.info("EchoCare is thinking…")
        reply = generate_reply(user_text)

    # --------------------------
    # 🔹 Crisis UI handler (always after reply)
    # --------------------------
    if "Are you in a safe place" in reply:
        st.error("⚠️ Crisis detected — please read carefully:")
        st.markdown(reply)
        st.warning("You matter. If you're in immediate danger, call your local emergency helpline.")
    else:
        st.markdown("### 🌿 EchoCare:")
        st.write(reply)

    # Save conversation
    st.session_state.chat_history.append({"role": "user", "text": user_text})
    st.session_state.chat_history.append({"role": "assistant", "text": reply})

    # --------------------------
    # 🔹 Voice Output (Murf)
    # --------------------------
    try:
        st.info("🎶 Generating voice response...")
        out = murf_tts(reply)
        st.success("Voice ready — playing now!")
        play_audio(out)
    except Exception as e:
        st.error(f"Voice generation failed: {e}")

# --------------------------
# 🔹 Conversation History
# --------------------------
st.markdown("---")
st.subheader("📝 Conversation History")

if not st.session_state.chat_history:
    st.write("Your conversation will appear here.")
else:
    for msg in st.session_state.chat_history:
        if msg["role"] == "user":
            st.markdown(f"**🧍 You:** {msg['text']}")
        else:
            st.markdown(f"**🤍 EchoCare:** {msg['text']}")

# --------------------------
# Footer
# --------------------------
st.markdown("---")
st.caption("EchoCare is not a medical system. If you're in crisis, contact a trusted person or a local helpline immediately.")
