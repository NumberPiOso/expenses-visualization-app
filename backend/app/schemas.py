"""To avoid confusion between the SQLAlchemy models and the Pydantic models,
we will have the file models.py with the SQLAlchemy models, and the file schemas.py
with the Pydantic models.

These Pydantic models define more or less a "schema" (a valid data shape).

So this will help us avoiding confusion while using both.
"""
from enum import Enum
from typing import Optional

from pydantic import BaseModel


# class Item(str, Enum):
#     Income = "Income"
#     Expense = "Expense"


class MoveBase(BaseModel):
    type_move: str
    # subitem: SubItem  # Pending to define
    value: int
    description: Optional[str] = None


class MoveCreate(MoveBase):
    pass


class Move(MoveBase):
    id: int

    class Config:
        orm_mode = True
