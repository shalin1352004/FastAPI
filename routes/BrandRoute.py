
from fastapi import FastAPI,APIRouter
app=FastAPI()
from controllers.BrandController import add_brand
from models.BrandModel import Brand
router=APIRouter()

@router.post("/add-brand")
async def addBrand(brand:Brand):
	return await add_brand(brand) #route logic



	