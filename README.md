# Web Perpetual Calendar

Prototype FastAPI application that will calculate the Four Pillars (천간지지) for a given date and time.

## Development

```bash
uv venv
uv pip install -e .[dev]
pre-commit install
pytest
uvicorn app.main:app --reload
```
