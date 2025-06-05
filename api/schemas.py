""" Define how the data will be sent and received

    The schemas defined in here are for two objects:
        > TodoList
        > TodoItem
"""

from pydantic import BaseModel
from typing import Optional


######## TodoList schemas
class TodoListBase(BaseModel): name: str  # Defines the attributes a TodoList requires

class TodoListCreate(TodoListBase): pass  # Inherits the required attributes from TodoListBase

class TodoListUpdate(BaseModel): name: Optional[str] = None  # Optional for partial updates


class TodoListOut(TodoListBase):
    id: int

    class Config: orm_mode = True  # So Pydantic works with SQLAlchemy models
########


######## TodoItem schemas
class StatusEnum(str, Enum):
    NOT_STARTED = "Not started"
    IN_PROGRESS = "In progress"
    FINISHED    = "Finished"


class TodoItemBase(BaseModel):
    list_id     : int
    description : str
    status      : StatusEnum = StatusEnum.NOT_STARTED


class TodoItemCreate(TodoItemBase): pass  # Inherits all required fields


class TodoItemUpdate(BaseModel):
    description : Optional[str]        = None
    status      : Optional[StatusEnum] = None


class TodoItemOut(TodoItemBase):
    task_id : int

    class Config: orm_mode = True
########
