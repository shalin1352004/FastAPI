from fastapi import APIRouter
from controllers.TestController import add_test_data
from controllers.TestController import delete_test_data
from controllers.TestController import get_all_tests
from controllers.TestController import get_test_by_id
from bson import ObjectId
router=APIRouter()
from models.TestModel import Test
@router.post("/add-test")
async def add_test(test:Test):
    return await add_test_data(test)

@router.delete("/delete-test/{test_id}")
async def delete_test(test_id: str):
    return await delete_test_data(test_id)


@router.get("/test")
async def Alltest():
    return await get_all_tests()

@router.get("/get-test-by-id/{test_id}")
async def GetTestById(test_id: str):
    return await get_test_by_id(test_id)