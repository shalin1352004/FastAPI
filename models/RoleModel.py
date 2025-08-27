from pydantic import BaseModel,Field

class Role(BaseModel):
    type: str
    description: str
    permissions: list[str]
    is_active: bool 