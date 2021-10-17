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


@app.get("/models/{move_type}")
async def get_model(move_type: Item):
    return {"model_name": move_type, "message": "Deep Learning FTW!"}


@app.get("/items/{item_id}")
async def read_item(item_id):
    return {"item_id": item_id}


@app.get("/items/")
async def read_item(skip: int = 0, limit: int = 10):
    return fake_moves_db[skip : skip + limit]


@app.post("/items/")
async def create_item(item: Move):
    item_dict = item.dict()
    fake_moves_db.append(item)
    return item_dict
