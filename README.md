
# 📚 RAG-based Question Answering System (FastAPI + LangChain)

This is a lightweight **Retrieval-Augmented Generation (RAG)** application built with **FastAPI**. It allows you to query a set of documents (PDFs or text files), which are embedded into a vector store and used to answer questions with reference to their source documents.

---

## 🚀 Features

- Upload documents in `data/` folder (PDF or TXT).
- Uses Hugging Face models for embeddings.
- Uses Ollama models for LLM (Locally hosted).
- FAISS as the vector store.
- Async FastAPI backend with test suite.
- Simple JSON API interface.

---

## 🛠️ Setup Instructions

### 1. Clone the Repo

```bash
git clone <your-repo-url>
cd <your-project-folder>
```

### 2. Create and Activate a Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 📥 Model Setup

### 4. Install Ollama

Install [Ollama](https://ollama.com/download) and start the service:

```bash
ollama serve
```

### 5. Pull a Model (example: Gemma)

```bash
ollama pull gemma:2b
```

> You can choose any compatible model supported by `langchain-ollama`.

---

## 🔐 Configure Environment

Create a `.env` file in the root directory based on `.sample.env`:

```bash
cp .sample.env .env
```

Edit `.env`:

```env
OLLAMA_MODEL=gemma:2b
HUGGING_FACE_MODEL=all-MiniLM-L6-v2
```

---

## 📂 Add Documents

Place your `.pdf` or `.txt` files inside the `data/` folder. These will be indexed automatically on first run.

---

## ▶️ Run the Application

```bash
uvicorn main:app --reload
```

Visit: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) to test the `/ask` endpoint using Swagger UI.

---

## ✅ Example Request

**POST** `/ask`

```json
{
  "question": "What is The Metamorphosis about?"
}
```

**Response:**

```json
{
  "answer": "The Metamorphosis is about a man who turns into a bug...",
  "references": ["metamorphosis.pdf - Page 1"]
}
```

---

## 🧪 Run Tests

```bash
pytest
```

> Ensure the server isn't running during tests.

---

## 📌 Notes

- The vector store is persisted in the `faiss_index/` directory.
- It won’t re-index documents unless the folder is deleted or updated manually.
- Ensure you have enough memory to run Ollama models locally.
- You can use any Hugging Face sentence transformer model for embeddings.

---

## 🧹 Cleaning Up

To regenerate embeddings (e.g., if you change documents):

```bash
rm -rf faiss_index/
```

Then rerun the app — vector store will be rebuilt.
