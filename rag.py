import os
from dotenv import load_dotenv

from langchain_ollama import ChatOllama
from langchain.chains import ConversationalRetrievalChain
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_core.chat_history import InMemoryChatMessageHistory
from vector_store import get_vector_store

load_dotenv()

global_memory = InMemoryChatMessageHistory()

def get_message_history():
    return global_memory

def get_qa_chain():
    model_name = os.getenv("OLLAMA_MODEL", "gemma:2b")

    llm = ChatOllama(model=model_name)
    vectorstore = get_vector_store()

    base_chain = ConversationalRetrievalChain.from_llm(
        llm=llm,
        retriever=vectorstore.as_retriever(),
        return_source_documents=True
    )

    qa_chain = RunnableWithMessageHistory(
        base_chain,
        get_message_history,
        input_messages_key="question",
        history_messages_key="chat_history"
    )

    return qa_chain
