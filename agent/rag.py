import os
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS


def setup_rag():
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    KB_PATH = os.path.join(BASE_DIR, "data", "knowledge_base.md")

    loader = TextLoader(KB_PATH)
    documents = loader.load()

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50
    )
    chunks = splitter.split_documents(documents)

    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    vectorstore = FAISS.from_documents(chunks, embeddings)
    return vectorstore


def get_rag_answer(vectorstore, query: str) -> str:
    retriever = vectorstore.as_retriever()
    docs = retriever.invoke(query)


    if not docs:
        return "Sorry, I couldn't find relevant information."

    return docs[0].page_content

