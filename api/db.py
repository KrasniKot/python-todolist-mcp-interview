""" This file contains configurations for the DB connection """

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base


# SQLite database URL (file-based)
DATABASE_URL = "sqlite:///./todo.sqlite3"

# Create the engine (connect_args is specific to SQLite)
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

# Create a configured "Session" class
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db():
    """ Yields a Session object and then closses it """
    db: Session = SessionLocal()
    try: yield db
    finally: db.close()


# Base class for your models
Base = declarative_base()
