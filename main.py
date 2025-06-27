from fastapi import FastAPI
from pydantic import BaseModel
from rag import get_qa_chain

app = FastAPI()
qa_chain = get_qa_chain()

class Query(BaseModel):
    question: str

class Answer(BaseModel):
    answer: str

@app.post("/ask", response_model=Answer)
async def ask_question(query: Query):
    answer = qa_chain.invoke({"question": query.question})["answer"]
    return {"answer": answer}
