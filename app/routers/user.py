from fastapi import APIRouter
import asyncio
router2 = APIRouter(prefix='/user', tags=['user'])

@router2.get("/")
async def all_user():
    pass

@router2.get("/user_id")
async def user_by_id():
    pass

@router2.post("/create")
async def crate_user():
    pass

@router2.put("/update")
async def update_user():
    pass

@router2.delete("/update")
async def delete_user():
    pass