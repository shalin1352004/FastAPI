from fastapi import APIRouter
from controllers.RoleController import create_role
from controllers.RoleController import get_roles
from controllers.RoleController import delete_role
from models.RoleModel import Role
router = APIRouter()
@router.post("/create-role")
async def createrole(role: Role):
    return await create_role(role)


@router.get("/roles")
async def getroles():
    return await get_roles()

@router.delete("/delete-roles")
async def deleteroles():
    return await delete_role()