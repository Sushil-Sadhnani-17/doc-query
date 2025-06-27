import os
from langchain_community.document_loaders import PyMuPDFLoader, TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter

def load_documents(folder_path):
    docs = []
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        if filename.endswith(".pdf"):
            loader = PyMuPDFLoader(file_path)
        elif filename.endswith(".txt"):
            loader = TextLoader(file_path, encoding='utf-8')
        else:
            continue
        loaded_docs = loader.load()
        for doc in loaded_docs:
            if doc.metadata.get("page") is not None:
                doc.metadata["source"] = f"{filename} - Page {doc.metadata['page']}"
            else:
                doc.metadata["source"] = filename
            docs.append(doc)

    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    return splitter.split_documents(docs)
