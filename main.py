from fastapi import FastAPI
from contextlib import asynccontextmanager

from database import create_tables, delete_tables
from router import router as tasks_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    print("DB cleared")
    await delete_tables() # delete tables
    print("DB created")
    await create_tables() # creating tables
    yield
    print('Выключения')

app = FastAPI(lifespan=lifespan)
app.include_router(tasks_router)
