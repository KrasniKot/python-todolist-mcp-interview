""" Routes for todo items

    Includes routes for:
        > Creation
        > Retrieval (all and by ID)
        > Updating
        > Deletion
"""

from fastapi import APIRouter, Depends, HTTPException

from sqlalchemy.orm import Session

from ..crud import TodoItemCRUD, TodoListCRUD
from ..schemas import TodoItemCreate, TodoItemUpdate, TodoItemOut
from ..db import get_db


router = APIRouter()


@router.post("/", response_model=TodoItemCreate)
def create_todoitem(data: TodoItemCreate, db: Session = Depends(get_db)):
    """ Creates a new todo item """
    # Check list exists
    if not TodoListCRUD(db).get(data.list_id): raise HTTPException(status_code=404, detail=f"TodoList with id <{data.list_id}> was not found")

    return TodoItemCRUD(db).create(data)


@router.get("/", response_model=list[TodoItemOut])
def read_todoitems(db: Session = Depends(get_db)):
    """ Gets all todo items"""
    return TodoItemCRUD(db).get_all()


@router.get("/{todoitem_id}", response_model=TodoItemOut)
def read_todoitem(todoitem_id: int, db: Session = Depends(get_db)):
    """ Gets a specific todo item by its ID """
    todoitem = TodoItemCRUD(db).get(todoitem_id)

    if todoitem is None: raise HTTPException(status_code=404, detail=f"Todo item with id <{todoitem_id}> was not found")

    return todoitem


@router.put("/{todoitem_id}", response_model=TodoItemUpdate)
def update_todoitem(todoitem_id: int, update_data: TodoItemUpdate, db: Session = Depends(get_db)):
    """ Updates a todo item by its ID """
    # Check if list_id was actually provided in the request
    update_dict = update_data.dict(exclude_unset=True)
    
    if 'list_id' in update_dict:
        if TodoListCRUD(db).get(update_data.list_id) is None: 
            raise HTTPException(status_code=404, detail=f"List with id <{update_data.list_id}> was not found")

    todoitem = TodoItemCRUD(db).update(todoitem_id, update_data)

    if todoitem is None: raise HTTPException(status_code=404, detail=f"Todo item with id <{todoitem_id}> was not found")

    return todoitem


@router.delete("/{todoitem_id}", response_model=bool)
def delete_todoitem(todoitem_id: int, db: Session = Depends(get_db)):
    """ Deletes a todo item by its ID """
    todoitem = TodoItemCRUD(db).delete(todoitem_id)

    if todoitem is None: raise HTTPException(status_code=404, detail=f"Todo item with id <{todoitem_id}> was not found")

    return todoitem
