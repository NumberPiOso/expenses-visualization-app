from enum import Enum
from typing import List, Optional

import uvicorn
from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from . import crud, models, schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)


app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
async def root():
    return {"hello": "Main page"}


@app.get("/move/{move_id}")
async def read_item(move_id):
    return {"move_id": move_id}


@app.get("/move/", response_model=List[schemas.Move])
def read_moves(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    moves = crud.get_moves(db, skip=skip, limit=limit)
    return moves


@app.post("/move/", response_model=schemas.Move)
async def create_item(move: schemas.MoveCreate, db: Session = Depends(get_db)):
    move_dict = crud.create_move(db, move)
    return move_dict


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
