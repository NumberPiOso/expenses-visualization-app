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

## Docker

Build backend docker app

```Bash
docker build -t expenses-backend .
```

and run it

```Bash
docker run -d -p 80:80 expenses-backend
```