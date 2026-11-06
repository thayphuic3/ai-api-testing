import re

STOPWORDS = {
    "a", "an", "the", "is", "are", "was", "were",
    "to", "of", "in", "on", "and", "or", "for",
    "that", "this", "it", "as", "by", "with",
    "what", "how", "does", "do", "can", "be",
    "using", "used"
}


def tokenize(text: str) -> set[str]:
    """Normalize text and return meaningful tokens."""
    if not text:
        return set()

    words = re.findall(r"\b[a-z0-9]+\b", text.lower())

    return {
        word for word in words
        if word not in STOPWORDS
    }


def calculate_f1(reference: str, answer: str) -> float:
    """Calculate token-level F1 similarity."""
    reference_tokens = tokenize(reference)
    answer_tokens = tokenize(answer)

    if not reference_tokens or not answer_tokens:
        return 0.0

    common = reference_tokens & answer_tokens

    precision = len(common) / len(answer_tokens)
    recall = len(common) / len(reference_tokens)

    if precision + recall == 0:
        return 0.0

    return round(
        2 * precision * recall / (precision + recall) * 100,
        2
    )


def calculate_relevance(question: str, answer: str) -> float:
    """Measure question keyword coverage in the answer."""
    question_tokens = tokenize(question)
    answer_tokens = tokenize(answer)

    if not question_tokens or not answer_tokens:
        return 0.0

    common = question_tokens & answer_tokens

    return round(
        len(common) / len(question_tokens) * 100,
        2
    )


def calculate_faithfulness(context: str, answer: str) -> float:
    """Measure how much answer vocabulary is supported by context."""
    context_tokens = tokenize(context)
    answer_tokens = tokenize(answer)

    if not answer_tokens:
        return 0.0

    if not context_tokens:
        return 0.0

    common = context_tokens & answer_tokens

    return round(
        len(common) / len(answer_tokens) * 100,
        2
    )


def calculate_hallucination(faithfulness: float) -> float:
    """Estimate unsupported vocabulary ratio."""
    return round(100 - faithfulness, 2)