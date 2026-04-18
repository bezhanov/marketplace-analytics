from pydantic import EmailStr, BaseModel
from sqlmodel import SQLModel, Field

class User(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    email: EmailStr
    first_name: str
    last_name: str
    role: str

class UserCreate(BaseModel):
    email: EmailStr
    first_name: str
    last_name: str
    role: str