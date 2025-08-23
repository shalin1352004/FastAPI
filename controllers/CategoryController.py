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