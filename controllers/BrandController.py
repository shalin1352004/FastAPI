
from models.BrandModel import Brand
from config.database import brand_collection

async def add_brand(brand: Brand):
	result = brand_collection.insert_one(brand.dict())
	return {**brand.dict}

async def get_brands():
    brands = await brand_collection.find().to_list(1000)
    return [Brand(**brand) for brand in brands]