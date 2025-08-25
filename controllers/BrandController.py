
from models.BrandModel import Brand
from config.database import brand_collection

async def add_brand(brand: Brand):
	result = brand_collection.insert_one(brand.dict())
	return {**brand.dict}