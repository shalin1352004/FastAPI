from fastapi import APIRouter
from models.ItemModel import Item
from controllers.ItemController import create_item
from controllers.ItemController import get_item
router = APIRouter()
@router.post("/addItem")
async def add_item(item: Item):
    return await create_item(item)
@router.get("/allItems")
async def get_all_items():
    return await get_item()
    
