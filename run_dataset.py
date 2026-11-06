from app.data_loader import load_test_cases

df = load_test_cases("datasets/chat_test_cases.csv")

print("Total test cases:", len(df))

print("\nDataset:")
print(df)

print("\nTest cases by category:")
print(df["category"].value_counts())

print("\nExpected status distribution:")
print(df["expected_status"].value_counts())