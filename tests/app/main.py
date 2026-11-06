from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(
    title="AI API Testing Demo",
    version="1.0.0"
)


class ChatRequest(BaseModel):
    question: str


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }


@app.post("/chat")
def chat(request: ChatRequest):

    question = request.question.strip()

    if not question:
        return {
            "answer": "",
            "status": "error"
        }

    return {
        "answer": f"Mock AI response: {question}",
        "status": "success"
    }