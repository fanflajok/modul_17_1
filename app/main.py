from fastapi import FastAPI
from routers import user
from routers import task
import asyncio


fapp = FastAPI()
greeting = {'message': 'Welcome to Taskmanager'}


@fapp.get("/")
async def welcome_def():
    return greeting

fapp.include_router(task.router1)
fapp.include_router(user.router2)

