from models.ItemModel import Item
from config.database import db
async def create_item(item: Item):
    result = await db.items.insert_one(item.dict())
    return {**item.dict()}

# ...existing code...
async def get_item():
    items = await db.items.find().to_list(1000)
    return [Item(**item) for item in items]
# ...existing code...