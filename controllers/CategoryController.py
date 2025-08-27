from models.CategoryModel import Category
from config.database import category_collection

async def create_category(category: Category):
    existing = await category_collection.find_one({"title": category.title})
    if existing:
        return {"error": "Category with this title already exists."}
    result = await category_collection.insert_one(category.dict())
    return {**category.dict()}

async def get_categories():
    result = await category_collection.find().to_list(1000)
    return [Category(**category) for category in result]

async def delete_category(title: str):
    result = await category_collection.delete_one({"title": title})
    print(result)
    return {"message": "Category deleted successfully"}
from models.CategoryModel import Category
from config.database import category_collection
from bson import ObjectId  # Add this import

# ...existing code...

async def get_category_by_category_id(category_Id: str):
    try:
        obj_id = ObjectId(category_Id)
    except Exception:
        return {"error": "Invalid category ID format"}
    category = await category_collection.find_one({"_id": obj_id})
    if category:
        category.pop("_id", None)  
        return Category(**category)
    return None