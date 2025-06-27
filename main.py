from typing import List

from fastapi import FastAPI
from pydantic import BaseModel
from rag import get_qa_chain

app = FastAPI()
qa_chain = get_qa_chain()

class Query(BaseModel):
    question: str

class Answer(BaseModel):
    answer: str
    references: List[str]

@app.post("/ask", response_model=Answer)
async def ask_question(query: Query):
    result = qa_chain.invoke({"question": query.question})
    answer = result["answer"]
    sources = result.get("source_documents", [])

    references = list({doc.metadata.get("source", "Unknown") for doc in sources})
    return {"answer": answer, "references": references}
