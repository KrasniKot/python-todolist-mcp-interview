""" Define how the data will be sent and received

    The schemas defined in here are for two objects:
        > TodoList
        > TodoItem
"""

from pydantic import BaseModel, field_validator
from typing import Optional

from api.enums import StatusEnum

######## TodoList schemas
class TodoListBase(BaseModel):
    name: str  # Defines the attributes a TodoList requires

    @field_validator('name')
    def validate_name(cls, v):
        """ Validate the name field """
        if not v or not v.strip(): raise ValueError('Name cannot be empty')

        return v

class TodoListCreate(TodoListBase): pass  # Inherits the required attributes from TodoListBase

class TodoListUpdate(BaseModel): name: Optional[str] = None  # Optional for partial updates


class TodoListOut(TodoListBase):
    id: int

    class Config: orm_mode = True  # So Pydantic works with SQLAlchemy models
########


######## TodoItem schemas
class TodoItemBase(BaseModel):
    list_id     : int
    description : str
    status      : StatusEnum = StatusEnum.NOT_STARTED

    @field_validator('description')
    def valiate_description(cls, v):
        """ Validate the description field """
        if not v or not v.strip(): raise ValueError('Description cannot be empty')

        return v

class TodoItemCreate(TodoItemBase): pass  # Inherits all required fields


class TodoItemUpdate(BaseModel):
    description : Optional[str]        = None
    status      : Optional[StatusEnum] = None


class TodoItemOut(TodoItemBase):
    id: int

    class Config: orm_mode = True
########
