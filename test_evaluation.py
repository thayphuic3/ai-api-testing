from evaluation.evaluator import evaluate_answer


question = "What is API testing?"

expected_answer = (
    "API testing verifies that an API works correctly "
    "and meets requirements"
)

context = (
    "API testing checks endpoints requests responses "
    "and expected behavior"
)

answer = (
    "API testing verifies that an API works correctly "
    "and checks endpoints and responses"
)

result = evaluate_answer(
    question=question,
    answer=answer,
    expected_answer=expected_answer,
    context=context,
)

print("\nAI EVALUATION RESULT")
print("====================")

for metric, score in result.items():
    print(f"{metric}: {score}")