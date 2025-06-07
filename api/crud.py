""" Contains the CRUD functions that perform the actual interaction with the db """

from typing import List, Optional, TypeVar, Generic, Type

from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError

from api.models import TodoList, TodoItem
from api.schemas import *

from pydantic import BaseModel



T = TypeVar("T")                   # SQLAlchemy model type
C = TypeVar("C", bound=BaseModel)  # Pydantic create schema
U = TypeVar("U", bound=BaseModel)  # Pydantic update schema


class BaseCRUD(Generic[T, C, U]):
    """ Defines generic CRUD functions to be re-utilised by TodoList and TodoItem """

    def __init__(self, db: Session, model: Type[T]):
        """ Initialises a BaseCRUD class
            > db ....... db session to execute queries
            > model .... class for which the functions will be executed
        """
        self.db    = db
        self.model = model


    def create(self, obj_in: C) -> T:
        """ Creates a new object
            > obj_in .... object information

            >>> Created Object
        """
        db_obj = self.model(**obj_in.dict())

        try:
            self.db.add(db_obj)
            self.db.commit()
            self.db.refresh(db_obj)
            return db_obj

        except IntegrityError:
            self.db.rollback()  #rollback the session after error
            return None


    def get(self, obj_id: int) -> Optional[T]:
        """ Fetches an object based on its ID
            > obj_id .... id of the object to be fetched

            >>> Object, if found
        """
        return self.db.query(self.model).filter(self.model.id == obj_id).first()


    def get_all(self, skip: int = 0, limit: int = 100) -> List[T]:
        """ Fetches all the items from a class
            > skip ..... index to start from
            > limit .... last index - 1 to be included

            >>> Objects found between skip > index > skip + limit
        """
        return self.db.query(self.model).offset(skip).limit(limit).all()


    def update(self, obj_id: int, obj_in: U) -> Optional[T]:
        """ Updates an object based on its ID
            > obj_id .... id of the object to be updated
            > obj_in .... information to update the object with

            >>> Updated object
        """
        db_obj = self.get(obj_id)

        if not db_obj: return None

        obj_data = obj_in.dict(exclude_unset=True)
        for field, value in obj_data.items(): setattr(db_obj, field, value)

        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj


    def delete(self, obj_id: int) -> bool:
        """ Deletes an object based on its id
            > obj_id .... id of the object to be deleted

            >>> Deleted object
        """
        db_obj = self.get(obj_id)
        if not db_obj: return None

        self.db.delete(db_obj)
        self.db.commit()

        return db_obj


class TodoListCRUD(BaseCRUD[TodoList, TodoListCreate, TodoListUpdate]):
    """ CRUD Operations for the TodoList class """
    def __init__(self, db: Session): super().__init__(db, TodoList)


    def get_items_list(self, list_id: int) -> List[TodoItem]:
        """ Fetches all todo items belonging to a specific list ID """
        if todolist:= self.get(list_id): return todolist.items
        return []


class TodoItemCRUD(BaseCRUD[TodoItem, TodoItemCreate, TodoItemUpdate]):
    """ CRUD Operations for the TodoItem class """
    def __init__(self, db: Session): super().__init__(db, TodoItem)
