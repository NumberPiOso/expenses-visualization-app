# BACKEND

Backend is being written in _Python_ and FastAPI.

To install environment get into this folder and run
```Bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

To run development server

```Bash
uvicorn app.main:app --reload
```