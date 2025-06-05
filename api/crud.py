""" Contains the CRUD functions that perform the actual interaction with the db """

from typing import List, Optional, TypeVar, Generic, Type
from sqlalchemy.orm import Session
from api.models import TodoList, TodoItem
from api.schemas import *
from pydantic import BaseModel


T = TypeVar("T")                   # SQLAlchemy model type
C = TypeVar("C", bound=BaseModel)  # Pydantic create schema
U = TypeVar("U", bound=BaseModel)  # Pydantic update schema


class BaseCRUD(Generic[T, C, U]):

    def __init__(self, db: Session, model: Type[T]):
        self.db    = db
        self.model = model


    def create(self, obj_in: C) -> T:
        db_obj = self.model(**obj_in.dict())
    
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
    
        return db_obj


    def get(self, obj_id: int) -> Optional[T]: return self.db.query(self.model).filter(self.model.id == obj_id).first()


    def get_all(self, skip: int = 0, limit: int = 100) -> List[T]: return self.db.query(self.model).offset(skip).limit(limit).all()


    def update(self, obj_id: int, obj_in: U) -> Optional[T]:
        db_obj = self.get(obj_id)

        if not db_obj: return None

        obj_data = obj_in.dict(exclude_unset=True)
        for field, value in obj_data.items(): setattr(db_obj, field, value)

        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj


    def delete(self, obj_id: int) -> bool:
        db_obj = self.get(obj_id)
        if not db_obj: return False

        self.db.delete(db_obj)
        self.db.commit()

        return True


class TodoListCRUD(BaseCRUD[TodoList, TodoListCreate, TodoListUpdate]):
    """ CRUD Operations for the TodoList class """
    def __init__(self, db: Session): super().__init__(db, TodoList)


class TodoItemCRUD(BaseCRUD[TodoItem, TodoItemCreate, TodoItemUpdate]):
    """ CRUD Operations for the TodoItem class """
    def __init__(self, db: Session): super().__init__(db, TodoItem)
