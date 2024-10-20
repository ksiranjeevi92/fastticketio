from contextlib import asynccontextmanager

from fastapi import FastAPI

from storeapi.database import database
from storeapi.routers.post import router as post_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    await database.connect()
    yield
    await database.disconnect()


app = FastAPI(lifespan=lifespan, title="Store API", version="0.0.1")

app.include_router(post_router, prefix="/posts")


@app.get("/")
async def root():
    return {"message": "hello world"}
