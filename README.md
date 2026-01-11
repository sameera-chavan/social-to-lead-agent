# Social-to-Lead Agentic Workflow – AutoStream

This project implements a GenAI-powered conversational agent for a fictional SaaS product called **AutoStream**, an automated video editing platform for content creators.

The agent is designed to:
- Answer product and pricing questions using Retrieval-Augmented Generation (RAG)
- Identify high-intent users
- Collect lead details through a multi-turn conversation
- Trigger a backend lead-capture tool only after all required details are collected

This project was built as part of the **Machine Learning Intern Assignment for ServiceHive**.

---

## Tech Stack
- Python 3.9+
- LangChain
- FAISS Vector Store
- HuggingFace Sentence Transformers (local embeddings)
- Modular conversational agent design

---

## How to Run the Project

```bash
git clone https://github.com/sameera-chavan/social-to-lead-agent.git
cd social-to-lead-agent
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python app.py

