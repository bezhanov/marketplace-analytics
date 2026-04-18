from app.models.User import User
from .engine import engine
from sqlmodel import Session, select


def get_user(user_id: int) -> User | None:
    """Return a user by ID, or None if no user is found."""
    with Session(engine) as session:
        return session.get(User, user_id)


def get_users() -> list[User]:
    """Return all users from the database."""
    with Session(engine) as session:
        statement = select(User)
        return session.exec(statement).all()


def create_user(user: User) -> User:
    """Create a user, persist it, and return the refreshed object."""
    with Session(engine) as session:
        session.add(user)
        session.commit()
        session.refresh(user)
        return user
