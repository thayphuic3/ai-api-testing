import pandas as pd

def load_test_cases(file_path):
    df = pd.read_csv(file_path)

    required_columns = [
        "test_id",
        "question",
        "expected_status",
        "category",
    ]

    for column in required_columns:
        if column not in df.columns:
            raise ValueError(f"Missing column: {column}")

    return df