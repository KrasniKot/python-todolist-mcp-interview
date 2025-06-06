""" Routes for todo items

    Includes routes for:
        > Creation
        > Retrieval (all and by ID)
        > Updating
        > Deletion
"""

from fastapi import APIRouter, Depends

from sqlalchemy.orm import Session

from ..crud import TodoItemCRUD
from ..db import SessionLocal
from ..schemas import TodoItemCreate, TodoItemUpdate
from ..db import get_db


router = APIRouter()
ticrud = TodoItemCRUD(SessionLocal)


@router.post("/")
def create_todoitem(data: TodoItemCreate, db: Session = Depends(get_db)):
    """ Creates a new todo item """
    ticrud  = TodoItemCRUD(db)

    return ticrud.create(data)


@router.get("/")
def read_todoitems(db: Session = Depends(get_db)):
    """ Gets all todo items"""
    ticrud = TodoItemCRUD(db)

    return {"items": ticrud.get_all()}


@router.get("/{todoitem_id}")
def read_todoitem(todoitem_id: int, db: Session = Depends(get_db)):
    """ Gets a specific todo item by its ID """
    ticrud = TodoItemCRUD(db)

    return {"item": ticrud.get(todoitem_id)}


@router.put("/{todoitem_id}")
def update_todoitem(todoitem_id: int, update_data: TodoItemUpdate, db: Session = Depends(get_db)):
    """ Updates a todo item by its ID """
    ticrud = TodoItemCRUD(db)

    return {"updateditem": ticrud.update(todoitem_id, update_data)}


@router.delete("/{todoitem_id}")
def delete_todoitem(todoitem_id: int, db: Session = Depends(get_db)):
    """ Deletes a todo item by its ID """
    ticrud = TodoItemCRUD(db)

    return {"deleteditem": ticrud.delete(todoitem_id)}
