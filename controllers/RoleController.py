from models.RoleModel import Role
from config.database import role_collection

async def create_role(role: Role):
    existing = await role_collection.find_one({"type": role.type})
    if existing:
        return {"error": "Role with this type already exists."}
    result = await role_collection.insert_one(role.dict())
    return {**role.dict()}

async def get_roles():
    roles = await role_collection.find().to_list(1000)
    return [Role(**role) for role in roles]

async def delete_role(type: str):
    result = await role_collection.delete_one({"type": type})
    print(result)
    return {"message": "Role deleted successfully"}