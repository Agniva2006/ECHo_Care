# Uses a lightweight HF emotion classifier, with a simple keyword fallback.
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch


MODEL_NAME = "j-hartmann/emotion-english-distilroberta-base"
try:
    tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
    model = AutoModelForSequenceClassification.from_pretrained(MODEL_NAME)
    model.eval()
except Exception as e:
    tokenizer = None
    model = None
    print("Deep emotion model failed to load — falling back to keyword detection", e)


KEYWORD_MAP = {
"sad": ["sad", "lonely", "depress", "cry"],
"anxious": ["anxious", "panic", "worried", "nervous"],
"angry": ["angry", "mad", "furious", "irritat"],
"joy": ["happy", "good", "joy", "grateful"],
"neutral": []
}




def deep_emotion_detect(text):
    text = (text or "").strip()
    if not text:
        return "neutral", {"neutral": 1.0}


    if tokenizer and model:
        try:
            inputs = tokenizer(text, return_tensors="pt", truncation=True)
            with torch.no_grad():
               logits = model(**inputs).logits
            probs = torch.softmax(logits[0], dim=0).cpu().numpy()
            labels = model.config.id2label
            scores = {labels[i].lower(): float(probs[i]) for i in range(len(probs))}
            top = max(scores, key=scores.get)
            return top, scores
        except Exception as e:
            print("HF emotion error", e)


# fallback keyword
    tl = text.lower()
    for k, words in KEYWORD_MAP.items():
        if any(w in tl for w in words):
            return k, {k: 1.0}
    return "neutral", {"neutral": 1.0}