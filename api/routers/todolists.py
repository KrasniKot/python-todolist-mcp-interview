""" Routes for todo lists

    Includes routes for:
        > Creation
        > Retrieval (all and by ID)
        > Updating
        > Deletion
"""

from fastapi import APIRouter, Depends, HTTPException

from sqlalchemy.orm import Session

from ..crud import TodoListCRUD
from ..db import SessionLocal
from ..schemas import TodoListCreate, TodoListUpdate, TodoListOut, TodoItemOut
from ..db import get_db


router = APIRouter()
tlcrud = TodoListCRUD(SessionLocal)


@router.post("/", response_model=TodoListCreate)
def create_todolist(data: TodoListCreate, db: Session = Depends(get_db)):
    """ Creates a new todo list """
    tlcrud  = TodoListCRUD(db)
    created = tlcrud.create(data)

    if created is None: raise HTTPException(status_code=404, detail=f"Todo llist with name '{data.name}', already exists")

    return created


@router.get("/", response_model=list[TodoListOut])
def read_todolists(db: Session = Depends(get_db)):
    """ Gets all todo lists"""
    tlcrud = TodoListCRUD(db)


    return tlcrud.get_all()


@router.get("/{todolist_id}", response_model=TodoListOut)
def read_todolist(todolist_id: int, db: Session = Depends(get_db)):
    """ Gets a specific todo list by its ID """
    todo_list = TodoListCRUD(db).get(todolist_id)

    if todo_list is None: raise HTTPException(status_code=404, detail="Todo list not found")

    return todo_list


@router.get("/{list_id}/items", response_model=list[TodoItemOut])
def get_items_for_list(list_id: int, db: Session = Depends(get_db)):
    """ Fetches all the items corresponding to a list """
    tlcrud  = TodoListCRUD(db)

    return tlcrud.get_items_list(list_id)


@router.put("/{todolist_id}", response_model=TodoListOut)
def update_todolist(todolist_id: int, update_data: TodoListUpdate, db: Session = Depends(get_db)):
    """ Updates a todo list by its ID """
    todo_list = TodoListCRUD(db).update(todolist_id, update_data)

    if todo_list is None: raise HTTPException(status_code=404, detail="Todo list not found")

    return todo_list


@router.delete("/{todolist_id}")
def delete_todolist(todolist_id: int, db: Session = Depends(get_db)):
    """ Deletes a todo list by its ID """
    todo_list = TodoListCRUD(db).delete(todolist_id)

    if todo_list is None: raise HTTPException(status_code=404, detail="Todo list not found")

    return todo_list
