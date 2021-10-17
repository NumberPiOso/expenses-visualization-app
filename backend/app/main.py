from enum import Enum
from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel


class Item(str, Enum):
    Income = "Income"
    Expense = "Expense"


class Move(BaseModel):
    id: int
    type_move: Item
    # subitem: SubItem  # Pending to define
    value: int
    description: Optional[str]


fake_moves_db = [
    Move(id=1, type_move="Income", value=100, description=""),
    Move(id=2, type_move="Expense", value=100),
]


app = FastAPI()


@app.get("/move/{move_id}")
async def read_item(move_id):
    return {"move_id": move_id}


@app.get("/move/")
async def read_item(skip: int = 0, limit: int = 10):
    return fake_moves_db[skip : skip + limit]


@app.post("/move/")
async def create_item(move: Move):
    move_dict = move.dict()
    fake_moves_db.append(move)
    return move_dict
