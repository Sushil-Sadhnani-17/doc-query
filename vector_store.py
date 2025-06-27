import os
from dotenv import load_dotenv

from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
from document_loader import load_documents

load_dotenv()

VECTOR_DIR = "faiss_index"

def get_vector_store():
    model_name = os.getenv("HUGGING_FACE_MODEL", "all-MiniLM-L6-v2")

    if os.path.exists(VECTOR_DIR):
        return FAISS.load_local(
            VECTOR_DIR,
            HuggingFaceEmbeddings(model_name=model_name),
            allow_dangerous_deserialization=True
        )

    documents = load_documents("data")
    embeddings = HuggingFaceEmbeddings(model_name=model_name)
    vectorstore = FAISS.from_documents(documents, embeddings)
    vectorstore.save_local(VECTOR_DIR)
    return vectorstore
