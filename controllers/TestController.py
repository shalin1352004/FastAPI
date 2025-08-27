from config.database import test_collection
from models.TestModel import Test
from bson import ObjectId
async def add_test_data(test: Test):
    result=await test_collection.insert_one(test.dict())
    return {"WELCOME"}

async def delete_test_data(test_id: str):
    result=await test_collection.delete_one({"_id":ObjectId(test_id)})
    return {"message":"Test data deleted successfully"}

async def get_all_tests():
    tests = await test_collection.find().to_list(1000)
    return [Test(**test) for test in tests]

async def get_test_by_id(test_id: str):
    result = await test_collection.find_one({"_id": ObjectId(test_id)})
    if result:  # Remove MongoDB _id field
        return Test(**result)
    return None