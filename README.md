# AI API Testing Demo

## Test Cases

| ID | Test Case | Input | Expected |
|---|---|---|---|
| TC01 | Health check | GET /health | 200 + healthy |
| TC02 | Valid question | "What is Python?" | 200 + success |
| TC03 | Empty question | "" | error |
| TC04 | Missing question | {} | 422 |
| TC05 | Invalid data type | 123 | 422 |
| TC06 | Unknown endpoint | /unknown | 404 |
| TC07 | Whitespace question | "   " | error |

