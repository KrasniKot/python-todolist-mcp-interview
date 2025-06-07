""" Define the db models

    > TodoList
    > TodoItem
"""

from sqlalchemy import Enum as SAEnum  # Alias to avoid clash
from sqlalchemy import Column, Integer, String, ForeignKey, Enum
from sqlalchemy.orm import relationship

from api.db import Base
from api.enums import StatusEnum


class TodoList(Base):
    """ Defines a todo list (a list of tasks) """

    __tablename__ = "todo_lists"

    id   = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, nullable=False)

    # Relationship to TodoItem
    items = relationship("TodoItem", back_populates="todo_list", cascade="all, delete-orphan")


class TodoItem(Base):
    """ Defines a todo item (a task) """
    __tablename__ = "todo_items"

    id          = Column(Integer, primary_key=True, index=True)
    list_id     = Column(Integer, ForeignKey("todo_lists.id"), nullable=False)
    description = Column(String, nullable=False)
    status      = Column(SAEnum(StatusEnum), default=StatusEnum.NOT_STARTED, nullable=False)

    # Relationship with TodoList
    todo_list = relationship("TodoList", back_populates="items")
