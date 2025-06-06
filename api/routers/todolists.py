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
from ..schemas import TodoListCreate, TodoListUpdate, TodoItemOut
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

    return {"lists": tlcrud.get_all()}


@router.get("/{todolist_id}")
def read_todolist(todolist_id: int, db: Session = Depends(get_db)):
    """ Gets a specific todo list by its ID """
    tlcrud = TodoListCRUD(db)

    return {"list": tlcrud.get(todolist_id)}


@router.get("/todolists/{list_id}/items", response_model=list[TodoItemOut])
def get_items_for_list(list_id: int, db: Session = Depends(get_db)):
    """ Fetches all the items corresponding to a list """
    crud  = TodoListCRUD(db)

    return crud.get_items_list(list_id)


@router.put("/{todolist_id}")
def update_todolist(todolist_id: int, update_data: TodoListUpdate, db: Session = Depends(get_db)):
    """ Updates a todo list by its ID """
    tlcrud = TodoListCRUD(db)

    return {"updatedlist": tlcrud.update(todolist_id, update_data)}


@router.delete("/{todolist_id}")
def delete_todolist(todolist_id: int, db: Session = Depends(get_db)):
    """ Deletes a todo list by its ID """
    tlcrud = TodoListCRUD(db)

    return {"deletedlist": tlcrud.delete(todolist_id)}
