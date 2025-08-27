from pydantic import BaseModel

class Category(BaseModel):
    title: str
    description: str
    category_id: str 
    

    