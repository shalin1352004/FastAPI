from pydantic import BaseModel
class User(BaseModel):
    name: str
    email: str
    password: str
    age: int
    is_active: bool = True
    is_admin: bool = False
    bio: str | None = None
