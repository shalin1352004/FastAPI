
from fastapi import FastAPI,APIRouter

from controllers.BrandController import add_brand
from controllers.BrandController import get_brands
from models.BrandModel import Brand
from bson import ObjectId
from controllers.BrandController import get_brand_by_id
router=APIRouter()
@router.post("/add-brand")
async def addBrand(brand:Brand):
	return await add_brand(brand) #route logic


@router.get("/get-brands")
async def getBrands():
	return await get_brands()

@router.get("/brand/{brand_id}")
async def getBrandById(brand_id: str):
	return await get_brand_by_id(ObjectId(brand_id))

