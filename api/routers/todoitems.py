"""Routes for todo items

    Includes routes for:
        > Creation
        > Retrieval (all and by ID)
        > Updating
        > Deletion
"""

from fastapi import APIRouter

router = APIRouter()


@router.post("/")
def create_todoitem():
    """Create a new todo item"""
    print("Creating a new todo item...")
    return {"message": "Todo item created"}


@router.get("/")
def read_todoitems():
    """Get all todo items"""
    print("Fetching all todo items...")
    return {"data": []}


@router.get("/{todoitem_id}")
def read_todoitem(todoitem_id: int):
    """Get a specific todo item by its ID"""
    print(f"Fetching todo item with ID {todoitem_id}...")
    return {"data": {"id": todoitem_id}}


@router.put("/{todoitem_id}")
def update_todoitem(todoitem_id: int):
    """Update a todo item by its ID"""
    print(f"Updating todo item with ID {todoitem_id}...")
    return {"message": f"Todo item {todoitem_id} updated"}


@router.delete("/{todoitem_id}")
def delete_todoitem(todoitem_id: int):
    """Delete a todo item by its ID"""
    print(f"Deleting todo item with ID {todoitem_id}...")
    return {"message": f"Todo item {todoitem_id} deleted"}
