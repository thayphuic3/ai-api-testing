from evaluation.metrics import (
    calculate_f1,
    calculate_relevance,
    calculate_faithfulness,
    calculate_hallucination,
)


def evaluate_answer(
    question: str,
    answer: str,
    expected_answer: str,
    context: str,
) -> dict:

    correctness = calculate_f1(
        expected_answer,
        answer
    )

    relevance = calculate_relevance(
        question,
        answer
    )

    faithfulness = calculate_faithfulness(
        context,
        answer
    )

    hallucination = calculate_hallucination(
        faithfulness
    )

    overall_score = round(
        correctness * 0.4
        + relevance * 0.3
        + faithfulness * 0.3,
        2
    )

    return {
        "correctness": correctness,
        "relevance": relevance,
        "faithfulness": faithfulness,
        "hallucination": hallucination,
        "overall_score": overall_score,
        "evaluation_result": (
            "PASS" if overall_score >= 65 else "FAIL"
        )
    }