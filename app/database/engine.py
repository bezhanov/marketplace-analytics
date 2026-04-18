import os

from sqlalchemy import text
from sqlalchemy.orm import Session
from sqlmodel import create_engine, SQLModel
from app.models.User import User

engine = create_engine(os.getenv("DATABASE_ENGINE", ""),
                       pool_size=os.getenv("DATABASE_POOL_SIZE", 10))

def create_db_and_tables():
    """Create all database tables defined in SQLModel metadata."""
    SQLModel.metadata.create_all(engine)

def check_availability():
    """Return True if the database is reachable, otherwise return False."""
    try:
        with Session(engine) as session:
            session.execute(text("SELECT 1"))
        return True
    except Exception as e:
        print(e)
        return False
