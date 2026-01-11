from agent.intent_classifier import classify_intent
from agent.rag import get_rag_answer
from agent.tools import mock_lead_capture


def handle_message(state, user_input, vectorstore):
    state["messages"].append(user_input)

    intent = classify_intent(user_input)
    state["intent"] = intent

    # Greeting
    if intent == "greeting":
        return "Hello! How can I help you with AutoStream today?"

    # Product inquiry → RAG
    if intent == "product_inquiry":
        return get_rag_answer(vectorstore, user_input)

    # High intent → lead capture flow
    if intent == "high_intent":

        if state["name"] is None:
            return "Great! May I know your name?"

        if state["email"] is None:
            state["name"] = user_input
            return "Thanks! Please share your email address."

        if state["platform"] is None:
            state["email"] = user_input
            return "Which platform do you create content on?"

        state["platform"] = user_input
        mock_lead_capture(state["name"], state["email"], state["platform"])

        return "Thank you! Our team will contact you shortly."

    return "How else can I assist you?"
