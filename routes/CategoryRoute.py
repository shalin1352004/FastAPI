from fastapi import APIRouter
from models.CategoryModel import Category
from controllers.CategoryController import get_categories
from controllers.CategoryController import create_category
from controllers.CategoryController import delete_category
router = APIRouter()

@router.post("/createCategory")
async def createCategory(category: Category):
    return await create_category(category)

@router.get("/getCategories")
async def getCategories():
    return await get_categories()


@router.delete("/delete-category/")
async def deletecategory():
    return await delete_category()