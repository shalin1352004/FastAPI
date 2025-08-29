from models.ItemModel import Item
from config.database import items_collection
from bson import ObjectId
async def create_item(item: Item):
    result = await items_collection.insert_one(item.dict())
    return {**item.dict()}

async def get_item():
    items = await items_collection.find().to_list(1000)
    return [Item(**item) for item in items]



async def get_item_by_id(item_id: str):
    result = await items_collection.find_one({"_id": ObjectId(item_id)})
    if result:
        result.pop("_id", None)  # Remove MongoDB _id field
        return Item(**result)
    return None


async def update_item(item_id: str, item: Item):
    result = await items_collection.update_one(
        {"_id": ObjectId(item_id)}, {"$set": item.dict()}
    )
    if result.modified_count:
        return {**item.dict()}
    return None                                 