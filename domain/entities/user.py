from pydantic import BaseModel, EmailStr, Field

class User(BaseModel):
    id: int
    username: str = Field(min_length=3, max_length=50)
    email: EmailStr
    first_name: str
    last_name: str