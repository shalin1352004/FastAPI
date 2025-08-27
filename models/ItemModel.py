from pydantic import BaseModel, Field
class Item(BaseModel):
    name: str
    description: str 
    price: float
    available_quantity: int
    in_stock: bool = Field(default=True)

