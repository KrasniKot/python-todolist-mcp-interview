""" Routes for todo items

    Includes routes for:
        > Creation
        > Retrieval (all and by ID)
        > Updating
        > Deletion
"""

from fastapi import APIRouter, Depends, HTTPException

from sqlalchemy.orm import Session

from ..crud import TodoItemCRUD
from ..db import SessionLocal
from ..schemas import TodoItemCreate, TodoItemUpdate, TodoItemOut
from ..db import get_db


router = APIRouter()
ticrud = TodoItemCRUD(SessionLocal)


@router.post("/", response_model=TodoItemOut)
def create_todoitem(data: TodoItemCreate, db: Session = Depends(get_db)):
    """ Creates a new todo item """
    return TodoItemCRUD(db).create(data)


@router.get("/", response_model=list[TodoItemOut])
def read_todoitems(db: Session = Depends(get_db)):
    """ Gets all todo items"""
    ticrud = TodoItemCRUD(db)

    return ticrud.get_all()


@router.get("/{todoitem_id}", response_model=TodoItemOut)
def read_todoitem(todoitem_id: int, db: Session = Depends(get_db)):
    """ Gets a specific todo item by its ID """
    todoitem = TodoItemCRUD(db).get(todoitem_id)

    if todoitem is None: raise HTTPException(status_code=404, detail=f"Todo item with id <{todoitem_id}> was not found")

    return todoitem


@router.put("/{todoitem_id}", response_model=TodoItemOut)
def update_todoitem(todoitem_id: int, update_data: TodoItemUpdate, db: Session = Depends(get_db)):
    """ Updates a todo item by its ID """
    todoitem = TodoItemCRUD(db).update(todoitem_id, update_data)

    if todoitem is None: raise HTTPException(status_code=404, detail=f"Todo item with id <{todoitem_id}> was not found")

    return todoitem


@router.delete("/{todoitem_id}", response_model=TodoItemOut)
def delete_todoitem(todoitem_id: int, db: Session = Depends(get_db)):
    """ Deletes a todo item by its ID """
    todoitem = TodoItemCRUD(db).delete(todoitem_id)

    if todoitem is None: raise HTTPException(status_code=404, detail=f"Todo item with id <{todoitem_id}> was not found")

    return todoitem
