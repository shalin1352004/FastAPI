from fastapi import HTTPException
from config.database import user_collection
from models.UserModel import User
from bson import ObjectId
async def get_user_by_id(email: str):
    user = await user_collection.find_one({"email": email})
    if user: # Remove MongoDB _id if you don't want to return it
        return User(**user)
    raise HTTPException(status_code=404, detail="User not found")

async def create_user(user: User):
    existing = await user_collection.find_one({"email": user.email})
    if existing:
        return {"error": "User with this email already exists."}
    result = await user_collection.insert_one(user.dict())
    return {**user.dict()}

async def getAllUsers():
	allUsers=await user_collection.find().to_list(1000)
	return [User(**user)for user in allUsers]


async def delete_user_by_id(user_id: str):
    result=await user_collection.delete_one({"_id":ObjectId(user_id)})
    if result.deleted_count==1:
        return {"message":"User deleted successfully"}
    return {"error":"User not found"}

