from fastapi import APIRouter
import asyncio
router1 = APIRouter(prefix='/task', tags=['task'])


@router1.get("/")
async def all_tasks():
    pass

@router1.get("/task_id")
async def task_by_id():
    pass

@router1.post("/create")
async def crate_task():
    pass

@router1.put("/update")
async def update_task():
    pass

@router1.delete("/update")
async def delete_task():
    pass