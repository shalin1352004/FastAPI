from fastapi import APIRouter
from controllers.UserController import create_user
from controllers.UserController import get_user_by_id
from controllers.UserController import getAllUsers
from models.UserModel import User
router = APIRouter()
@router.post("/create-user")
async def createuser(user: User):
    return await create_user(user)

@router.get("/user/{email}")
async def getuser(email: str):
    return await get_user_by_id(email)

@router.get("/allUsers")
async def getallusers():
    return await getAllUsers()