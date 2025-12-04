# utils/cbt.py — Safe CBT micro-reframe hints

def cbt_reframe(user_text: str) -> str:
    if not user_text:
        return ""

    t = user_text.lower()

    if "always" in t or "never" in t:
        return ("Sometimes when emotions become intense, our mind uses words like "
                "'always' or 'never'. It doesn’t mean the feeling isn’t real — "
                "but it may not reflect the full picture. Could we look for one exception?")

    if "my fault" in t or "it's my fault" in t or "its my fault" in t:
        return ("It sounds like you're taking on a lot of responsibility. "
                "Would you be open to exploring whether all of this is really on you?")

    if "ruin everything" in t or "i ruin everything" in t:
        return ("Feeling like you 'ruin everything' often comes from overwhelm, not fact. "
                "Can we pick one small recent moment to look at together?")

    return ""

