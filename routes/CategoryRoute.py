from fastapi import APIRouter
from models.CategoryModel import Category
from controllers.CategoryController import get_categories
from controllers.CategoryController import create_category
from controllers.CategoryController import delete_category
from controllers.CategoryController import get_category_by_category_id
router = APIRouter()
from bson import ObjectId
@router.post("/createCategory")
async def createCategory(category: Category):
    return await create_category(category)

@router.get("/getCategories")
async def getCategories():
    return await get_categories()


@router.delete("/delete-category/{title}")
async def deletecategory(title: str):
    return await delete_category(title)

@router.get("/category/{category_Id}")
async def getCategoryById(category_Id: str):
    return await get_category_by_category_id(ObjectId(category_Id))
