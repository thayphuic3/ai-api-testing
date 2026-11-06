
import pandas as pd
import httpx


def run_batch_tests(csv_path, api_url):
    df = pd.read_csv(csv_path, keep_default_na=False)

    results = []

    with httpx.Client(timeout=30.0) as client:
        for _, row in df.iterrows():

            test_id = row["test_id"]
            question = str(row["question"])

            expected_status = int(row["expected_status"])

            try:
                response = client.post(
                    api_url,
                    json={"question": question}
                )

                actual_status = response.status_code

                result = (
                    "PASS"
                    if actual_status == expected_status
                    else "FAIL"
                )

                error_message = ""

                if result == "FAIL":
                    error_message = response.text

            except httpx.RequestError as exc:
                actual_status = None
                result = "ERROR"
                error_message = str(exc)

            results.append({
                "test_id": test_id,
                "expected_status": expected_status,
                "actual_status": actual_status,
                "result": result,
                "error_message": error_message,
            })

    return pd.DataFrame(results)
