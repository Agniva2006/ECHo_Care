def detect_emotion(text):
    text_lower = text.lower()

    emo_map = {
        "sad": ["sad", "down", "hopeless", "depressed", "lonely"],
        "anxious": ["anxious", "worried", "scared", "fear", "panic"],
        "angry": ["angry", "mad", "frustrated", "rage"],
        "tired": ["tired", "exhausted", "drained"],
        "stressed": ["stress", "overwhelmed", "pressure"]
    }

    for emotion, words in emo_map.items():
        if any(w in text_lower for w in words):
            return emotion

    return "neutral"
