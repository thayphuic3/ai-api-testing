

from dotenv import load_dotenv
from google import genai
import os


# Đọc các biến môi trường từ file .env
load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")
MODEL_NAME = os.getenv("GEMINI_MODEL", "gemini-flash-latest")


class GeminiConfigurationError(Exception):
    """Lỗi cấu hình Gemini."""


class GeminiAPIError(Exception):
    """Lỗi khi giao tiếp với Gemini API."""


def generate_answer(question: str) -> str:
    """
    Gửi câu hỏi đến Gemini và trả về câu trả lời dạng text.
    """

    if not API_KEY:
        raise GeminiConfigurationError(
            "GEMINI_API_KEY is not configured."
        )

    try:
        # Dùng context manager để đóng client sau khi gọi API
        with genai.Client(api_key=API_KEY) as client:
            response = client.models.generate_content(
                model=MODEL_NAME,
                contents=question,
            )

        answer = response.text

        if not answer:
            raise GeminiAPIError(
                "Gemini returned an empty response."
            )

        return answer.strip()

    except GeminiAPIError:
        raise

    except Exception as exc:
        print("ERROR TYPE:", type(exc).__name__)
        print("ERROR MESSAGE:", str(exc))

        raise GeminiAPIError(
            f"Gemini request failed: {type(exc).__name__}"
        ) from None


#tạo mock LLM
def generate_mock_answer(question: str) -> str:
    """
    Generate a predictable response without calling Gemini.
    """
    if not question or not question.strip():
        raise ValueError("Question cannot be empty.")

    return (
        f"[MOCK AI RESPONSE] "
        f"This is a simulated answer for: {question}"
    )
