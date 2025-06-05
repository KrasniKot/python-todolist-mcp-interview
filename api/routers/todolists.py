""" Routes for todo lists

    Includes routes for:
        > Creation
        > Retrieval (all and by ID)
        > Updating
        > Deletion
"""

from fastapi import APIRouter


router = APIRouter()


@router.post("/")
def create_todolist():
    """Create a new todo list"""
    print("Creating a new todo list...")
    return {"message": "Todo list created"}


@router.get("/")
def read_todolists():
    """Get all todo lists"""
    print("Fetching all todo lists...")
    return {"data": []}


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
