"""To avoid confusion between the SQLAlchemy models and the Pydantic models,
we will have the file models.py with the SQLAlchemy models, and the file schemas.py
with the Pydantic models.

These Pydantic models define more or less a "schema" (a valid data shape).

So this will help us avoiding confusion while using both.
"""


import enum

from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Enum
from sqlalchemy.orm import relationship

from .database import Base


# class ItemModel(enum.Enum):
#     Income = "Income"
#     Expense = "Expense"


class Move(Base):
    __tablename__ = "movements"
    id = Column(Integer, primary_key=True, index=True)
    # type_move = Column(Enum(ItemModel), index=True)
    type_move = Column(String, index=True)
    value = Column(Integer, index=True)
    description = Column(String, index=True, nullable=True)
    # owner_id = Column(Integer, ForeignKey("users.id"))
    # owner = relationship("User", back_populates="items")
