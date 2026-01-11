import os
from dotenv import load_dotenv

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ENV_PATH = os.path.join(BASE_DIR, ".env")

load_dotenv(dotenv_path=ENV_PATH, override=True)

from agent.agent import handle_message
from agent.rag import setup_rag
from agent.agent import handle_message
from agent.rag import setup_rag

# Initialize RAG
vectorstore = setup_rag()

# Initial state
state = {
    "intent": None,
    "name": None,
    "email": None,
    "platform": None,
    "messages": []
}

print("AutoStream AI Agent is running. Type 'exit' to stop.\n")

while True:
    user_input = input("User: ")

    if user_input.lower() == "exit":
        break

    response = handle_message(state, user_input, vectorstore)
    print("Agent:", response)
