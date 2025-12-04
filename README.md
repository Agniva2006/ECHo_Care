🧠 README.md — EchoCare: Emotional Wellness Voice Companion
<div align="center"><h1>
🎧 EchoCare
A Voice-Based Emotional Wellness & Mental-Health Support Agent

Built with Llama 3.1 (8B) + Faster-Whisper + Murf Falcon TTS
Fully offline LLM + real-time voice + crisis-safe logic.
</h1>
</div>
🌟 Overview

EchoCare is an AI-powered emotional wellness companion designed to provide:

🗣️ Voice-based conversations

❤️ Emotion-aware responses

🛟 Crisis-safe support

🌬️ Breathing & grounding exercises

📝 Conversation memory

🎚️ Adaptive personality tones

🎶 Calming voice output via Murf AI

The system listens to the user’s voice, detects emotion, generates safe and empathetic responses using a local Llama-3.1 model, and replies with soothing Murf TTS audio.

EchoCare is not a clinical medical tool — it is a compassion companion, designed with safety and empathy.

🧩 Key Features
🔊 1. Real-Time Speech Interaction

Faster-Whisper ASR (base-int8)

Low-latency transcription

Handles noise and imperfect speech

❤️ 2. Deep Emotion Detection

EchoCare detects emotional categories:

anger

sadness

anxiety

fear

overwhelm

loneliness

neutral

And adjusts tone + response accordingly.

🛟 3. Trauma-Safe Crisis Mode (Crisis Override)

Instant detection of phrases like:

"I want to die"

"I can't take it anymore"

"I want to disappear"

"leap like this"

"end everything"

Triggers:

✔ Safety-first script
✔ Supportive grounding
✔ Encouragement to reach real help
✔ NO judgment
✔ NO medical advice
✔ NO assumptions

🧘 4. Built-in Emotional Tools

Users can say:

“Ground me”

EchoCare activates grounding:

Name 1 thing you can smell,
2 things you can touch,
3 things you can see...

“Calm me down / breathe / panic”

EchoCare activates breathing:

Inhale 4s → Hold 2s → Exhale 6s

🧠 5. CBT Micro-Reframes (Safe Cognitive Behavioral Hints)

Corrects harmful thinking patterns safely:

“I always ruin everything.”

“It’s all my fault.”

“Nothing ever works for me.”

EchoCare replies gently:

“Sometimes our mind uses words like always or never when we feel overwhelmed…”

No hallucinations.
No assumptions.
Evidence-based structure.

🗃️ 6. Conversation Memory

EchoCare remembers the last 20–50 user messages:

emotional patterns

frequently used tones

style adaptation

recurring concerns

Stored safely in data/user_profile.json.

🎭 7. Adaptive Personality Engine

EchoCare adapts tone based on user style:

Detected Style	Behavior
casual ("bro", "dude")	light, simple, friendly
reflective (long sentences)	deeper, slower tone
curious (many questions)	clear explanations
neutral	default calm tone
🎶 8. Calming Voice Output (Murf Falcon TTS)

Supports:

soft voice

warm voice

therapist voice

ASMR voice

friend voice

Audio returns as:

base64

or presigned Murf S3 URL

Then plays instantly in Streamlit.

📂 Project Structure
EchoCare/
│
├── main.py                      # Streamlit UI
├── llm_agent.py                 # Llama-based emotional response generator
├── asr.py                       # Speech-to-text using Faster-Whisper
├── tts_murf.py                  # Murf TTS wrapper
│
├── utils/
│   ├── audio.py                 # Recording + audio playback
│   ├── comfort.py               # Emotion→comfort phrase dictionary
│   ├── emotion.py               # Emotion classifier
│   ├── memory.py                # Persistent memory system
│   ├── personality.py           # Tone adaptation engine
│   ├── prompts.py               # EchoCare system prompt
│   ├── cbt.py                   # CBT micro-reframes
│
├── data/
│   └── user_profile.json        # Saved memory
│
├── .env                         # API keys + model names
├── requirements.txt             # All dependencies
└── README.md                    # Documentation

🚀 How It Works (System Pipeline)
User speaks → record_audio →
ASR (Faster-Whisper) → user_text →
Emotion detection →
Command detection →
LLM response generation (Llama 3.1 8B) →
Crisis override (if triggered) →
CBT hint + personality adaptation →
TTS generation (Murf AI) →
Audio playback →
Memory saved


Flow is fast, safe, and fully voice-based.

🛠️ Installation
1. Install requirements
pip install -r requirements.txt

2. Install Ollama + Llama 3.1
ollama pull llama3.1:8b

3. Add .env file
MURF_API_KEY=your_murf_key
OLLAMA_HOST=http://localhost:11434
OLLAMA_MODEL=llama3.1:8b
USER_ID=default_user

4. Run the app
streamlit run main.py

🔐 Safety Design

EchoCare follows:

Do-no-harm principle

No medical or diagnostic claims

Non-judgmental language

Professional crisis-handling tone

User privacy (local memory only)

Zero external LLM API usage (fully offline model)

🧪 Testing the System

Try saying:

Safe/Emotional:

“Everything feels heavy today.”

“I’m overwhelmed.”

“I feel lonely and numb.”

Panic / Anxiety:

“I can’t breathe.”

“My chest is tight.”

“I feel like I’m losing control.”

Crisis:

“I want to die.”

“I don’t want to live like this.”

“I want everything to end.”

“I want to commit suicide.”

Expected: Crisis override.

🎯 Goals & Motivation

EchoCare was created because millions struggle to express emotions aloud without judgment. A calm, safe voice companion can help people:

Feel heard

Feel grounded

Feel less alone

Self-regulate emotions

Reflect safely

EchoCare is not a doctor.
It is a compassion tool.

📌 Limitations

Not a replacement for therapy

Not a suicide hotline

Not a diagnostic tool

Accuracy depends on mic quality

Cannot detect self-harm intent with full certainty

Does not replace human connection

