from app.batch_runner import run_batch_tests

results = run_batch_tests(
    csv_path="datasets/chat_test_cases.csv",
    api_url="http://127.0.0.1:8000/chat"
)

print("\nBATCH TEST RESULTS")
print("=================")

print(results.to_string(index=False))

total = len(results)
passed = (results["result"] == "PASS").sum()
failed = (results["result"] == "FAIL").sum()
errors = (results["result"] == "ERROR").sum()

print("\nSUMMARY")
print("=======")
print("Total:", total)
print("Passed:", passed)
print("Failed:", failed)
print("Errors:", errors)

print("Pass Rate:", f"{passed / total * 100:.2f}%")