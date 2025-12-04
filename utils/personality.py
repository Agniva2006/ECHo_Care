# utils/personality.py — Personal tone adaptation for EchoCare

def detect_user_style(history_list):
    text = " ".join(history_list[-10:]).lower()

    if "bro" in text or "dude" in text:
        return "casual"

    # if user writes long sentences
    if any(len(sent.split()) > 25 for sent in history_list[-10:]):
        return "reflective"

    # if user asks many questions
    if text.count("?") > 2:
        return "curious"

    return "neutral"


def adapt_prompt_for_style(base_prompt, style):
    """Adds tone instructions to the prompt based on user style."""

    if style == "casual":
        return (
            base_prompt
            + "\nTone hint: Use simple, friendly language. Keep messages short and relaxed."
        )

    if style == "reflective":
        return (
            base_prompt
            + "\nTone hint: Use slightly longer reflective sentences and gentle language."
        )

    if style == "curious":
        return (
            base_prompt
            + "\nTone hint: Provide clear explanations with a calm, reassuring tone."
        )

    # default
    return base_prompt
