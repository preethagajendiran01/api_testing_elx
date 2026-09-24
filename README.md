# API Framework ELX

Tests JSONPlaceholder `/posts` using Python, pytest, requests and Pydantic.

## Structure
- `api/api_handler.py` - reusable GET/POST/PUT/DELETE methods
- `schemas/post_schema.py` - response schema validation
- `testdata/post_payloads.py` - request test data
- `tests/test_posts.py` - the 7 test cases
- `conftest.py` - shared `api_handler` fixture

## Local Configuration
 
For local execution, environment-specific values and API keys are kept in a .env file instead of hardcoding them in the Python code.
 
Example:
 
```text
BASE_URL=https://jsonplaceholder.typicode.com
API_TOKEN=
TIMEOUT=10
```

## Run
```bash
python -m venv .venv
# Windows: .venv\Scripts\activate
# macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
pytest
```

Priority runs:
```bash
pytest -m p1
pytest -m p2
```


