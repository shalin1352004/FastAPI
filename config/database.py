from motor.motor_asyncio import AsyncIOMotorClient

#db url
MONGO_URL = "mongodb://localhost:27017"
DATABASE_NAME ="LearningTool_db"
#database connection
client = AsyncIOMotorClient(MONGO_URL)
db = client[DATABASE_NAME]
#collections
items_collection = db["items"]
category_collection = db["category"]
role_collection = db["role"]
user_collection = db["user"]
brand_collection = db["brand"]