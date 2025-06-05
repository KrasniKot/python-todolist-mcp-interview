""" Routes for todo lists

    Includes routes for:
        > Creation
        > Retrieval (all and by ID)
        > Updating
        > Deletion
"""

from fastapi import APIRouter, Depends

from sqlalchemy.orm import Session

from ..crud import TodoListCRUD
from ..db import SessionLocal
from ..schemas import TodoListCreate
from ..db import get_db


router = APIRouter()
tlcrud = TodoListCRUD(SessionLocal)


@router.post("/")
def create_todolist(data: TodoListCreate, db: Session = Depends(get_db)):
    """ Creates a new todo list """
    tlcrud  = TodoListCRUD(db)

    return tlcrud.create(data)


@router.get("/")
def read_todolists(db: Session = Depends(get_db)):
    """ Gets all todo lists"""
    tlcrud = TodoListCRUD(db)

    return {"data": tlcrud.get_all()}


@router.get("/{todolist_id}")
def read_todolist(todolist_id: int):
    """Get a specific todo list by its ID"""
    print(f"Fetching todo list with ID {todolist_id}...")
    return {"data": {"id": todolist_id}}


@router.put("/{todolist_id}")
def update_todolist(todolist_id: int):
    """Update a todo list by its ID"""
    print(f"Updating todo list with ID {todolist_id}...")
    return {"message": f"Todo list {todolist_id} updated"}


@router.delete("/{todolist_id}")
def delete_todolist(todolist_id: int):
    """Delete a todo list by its ID"""
    print(f"Deleting todo list with ID {todolist_id}...")
    return {"message": f"Todo list {todolist_id} deleted"}
