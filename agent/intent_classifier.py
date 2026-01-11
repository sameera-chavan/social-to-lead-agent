def classify_intent(user_input: str) -> str:
    text = user_input.lower()

    if any(word in text for word in ["hi", "hello", "hey"]):
        return "greeting"

    if any(word in text for word in ["price", "pricing", "plan", "cost", "features"]):
        return "product_inquiry"

    if any(word in text for word in ["sign up", "try", "subscribe", "buy", "start"]):
        return "high_intent"

    return "product_inquiry"
