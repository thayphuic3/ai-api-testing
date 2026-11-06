# from fastapi import FastAPI, HTTPException
# from pydantic import BaseModel


# from app.services.llm_service import (
#     generate_answer,
#     GeminiConfigurationError,
#     GeminiAPIError,
# )

# app = FastAPI(
#     title="AI API Testing Demo",
#     version="2.0.0",
#     description="FastAPI application integrated with Google Gemini",
# )


# class ChatRequest(BaseModel):
#     question: str


# @app.get("/health")
# def health():
#     return {
#         "status": "healthy",
#         "service": "AI API Testing Demo",
#     }


# # @app.post("/chat")
# # def chat(request: ChatRequest):

# #     question = request.question.strip()

# #     if not question:
# #         return {
# #             "answer": "",
# #             "status": "error"
# #         }

# #     return {
# #         "answer": f"Mock AI response: {question}",
# #         "status": "success"
# #     }

# @app.post("/chat")
# def chat(request: ChatRequest):
#     question = request.question.strip()

#     # Kiểm tra câu hỏi không được rỗng
#     if not question:
#         raise HTTPException(
#             status_code=400,
#             detail="Question cannot be empty.",
#         )

#     try:
#         answer = generate_answer(question)

#         return {
#             "answer": answer,
#             "status": "success",
#         }

#     except GeminiConfigurationError:
#         raise HTTPException(
#             status_code=503,
#             detail="Gemini API is not configured.",
#         )

#     except GeminiAPIError:
#         raise HTTPException(
#             status_code=502,
#             detail="Unable to get a response from the AI provider.",
#         )


from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import os

from app.services.llm_service import (
    generate_answer,
    generate_mock_answer,
    GeminiConfigurationError,
    GeminiAPIError,
)


app = FastAPI(
    title="AI API Testing Demo",
    version="2.0.0",
    description="FastAPI application integrated with Google Gemini",
)


class ChatRequest(BaseModel):
    question: str


@app.get("/health")
def health():
    return {
        "status": "healthy",
        "service": "AI API Testing Demo",
    }



@app.post("/chat")
def chat(request: ChatRequest):
    question = request.question.strip()

    if not question:
        raise HTTPException(
            status_code=400,
            detail="Question cannot be empty."
        )

    llm_mode = os.getenv("LLM_MODE", "real").lower()

    try:
        if llm_mode == "mock":
            answer = generate_mock_answer(question)
        elif llm_mode == "real":
            answer = generate_answer(question)
        else:
            raise HTTPException(
                status_code=500,
                detail="Invalid LLM_MODE configuration."
            )

        return {
            "answer": answer,
            "status": "success",
            "mode": llm_mode
        }

    except GeminiConfigurationError:
        raise HTTPException(
            status_code=503,
            detail="Gemini API is not configured."
        )

    except GeminiAPIError:
        raise HTTPException(
            status_code=502,
            detail="Unable to get a response from the AI provider."
        )

