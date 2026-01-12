<h1>
🎧 EchoCare — Emotional Wellness Voice Companion
AI-Powered Mental Health Voice Assistant (Llama 3.1 + Faster-Whisper + Murf TTS)

</h1>
"D:\Games\FIFA 17\WhatsApp Video 2025-12-05 at 21.14.06_810f8248.mp4"
🌟 Overview

EchoCare is a voice-based emotional wellness assistant designed to provide:

✔ Supportive & empathetic conversation                                                                                            

✔ Emotion recognition

✔ Crisis-safe handling

✔ CBT-style guidance

✔ Grounding & breathing support

✔ Voice responses using Murf AI

✔ Memory-powered personalized interaction

The project runs 100% locally using:

1. Ollama (Llama 3.1 : 8B)

2. Faster-Whisper for real-time transcription

3.  Streamlit UI

4.  Murf AI for natural voice responses

🚀 Features
🧠 Core System

High-quality LLM responses (Llama 3.1:8b)

Faster-Whisper speech-to-text

Murf AI text-to-speech

Emotional tone detection

Comfort phrase auto-insertion

Conversation memory (last 5 user messages)

🛡️ Safety System

Suicide / self-harm phrase detection

Crisis-safe response protocol

Prevents harmful or unsafe replies

Emergency support suggestions

🌬️ Wellness Tools

Ground Me Mode (for dissociation)

Calm Me Mode (panic + breathing)

CBT reframing prompts

Personality adaptation

casual

reflective

curious

🏗️ Project Structure
EchoCare/
── main.py
│── asr.py
│── llm_agent.py
│── tts_murf.py
│── requirements.txt
│── README.md
│── .env
│
├── utils/
│   ├── audio.py
│   ├── prompts.py
│   ├── memory.py
│   ├── emotion.py
│   ├── comfort.py
│   ├── personality.py
│   ├── cbt.py
│   ├── deep_emotion.py
│   └── journal.py
│
└── data/
    ├── input.wav
    └── echocare_output.wav

💻         Installation (Local Machine)                                                                                                                                                                                              
1️.     Install dependencies pip install -r requirements.txt


2️.      Install & run Ollama

      🔗 Download Ollama:
      https://ollama.com/download
      
      Pull the model:
      
      ollama pull llama3.1:8b
      
      
      Start Ollama server:
      
      ollama serve

3.      Create .env file

        Create a new file named .env in the root folder:

OLLAMA_MODEL=llama3.1:8b
OLLAMA_HOST=http://localhost:11434
MURF_API_KEY=your_murf_api_key_here

4.       Run Streamlit app
        streamlit run main.py


Your application will open at:
👉 http://localhost:8501

🎤 How EchoCare Works
1️⃣ User Speaks

EchoCare records 6–8 seconds of audio.

2️⃣ Faster-Whisper Transcribes Speech

Audio → text.

3️⃣ Llama 3.1 Generates Safe Emotional Response

Replies are:

empathetic

calm

trauma-safe

personalized

4️⃣ Murf AI Converts Reply to Voice

Natural-sounding voice playback.

5️⃣ Memory & Emotion Tracking

EchoCare adapts to:

tone

past messages

emotional patterns

🔐 Safety & Crisis Handling

EchoCare automatically detects:

“I want to die”

“I will kill myself”

“End my life”

“I want to disappear”

“Suicidal thoughts”

It then responds with:

non-judgmental emotional support

grounding reminders

immediate safety instructions

encouraging the user to reach help

prevents harmful content

This ensures ethical, safe, responsible Mental Wellness AI.

🧪 Supported Voice Modes (Murf)
Mode	Voice ID	Description
Soft Female	en-IN-anisha	Warm, comforting
Calm Male	en-IN-nikhil	Gentle, emotional tone
Hindi Male	hi-IN-kabir	Native Hindi
Friendly Male	en-IN-samar	Casual Indian English

(You can modify these in tts_murf.py)

🙌 Why EchoCare?

Most mental health AI tools fail because they are:

❌ Unsafe

❌ Scripted

❌ Not emotional

❌ No real voice interaction

EchoCare changes everything:

✔ Real-time comforting voice

✔ Deep emotion recognition

✔ Trauma-safe logic

✔ Memory-powered personalization

✔ CBT-inspired reframing

✔ Smooth natural speech output

EchoCare is built to support, not diagnose.
It’s empathetic, responsible, and deeply human-like.

🚀 Future Roadmap

1.Deploy on HuggingFace Spaces / Render

2.Live streaming ASR

3.Mood tracking + analytics dashboard

4.Personal journal syncing

5.Mobile App (Flutter)

6.Multiple therapist personality modes

7.Daily emotional trend graph
