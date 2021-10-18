"""In this file we will have reusable functions to interact with the data in the database.

CRUD comes from: Create, Read, Update, and Delete.

By creating functions that are only dedicated to interacting with the database
(get a user or an item) independent of your path operation function, you can
more easily reuse them in multiple parts and also add unit tests for them.
"""
from sqlalchemy.orm import Session


from . import models, schemas


def get_moves(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Move).offset(skip).limit(limit).all()


def create_move(db: Session, move: schemas.MoveCreate):
    db_move = models.Move(**move.dict())
    db.add(db_move)
    db.commit()
    db.refresh(db_move)
    return db_move
