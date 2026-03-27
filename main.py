from contextlib import asynccontextmanager
from fastapi import FastAPI
from database import create_db_and_tables
from routers import products

@asynccontextmanager
async def lifespan(app: FastAPI):
    create_db_and_tables()
    yield

app = FastAPI(lifespan=lifespan)

@app.get("/")
def hello_world():
    return {"message": "Hello World"}

app.include_router(products.router, prefix="/products", tags=["products"])