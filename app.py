from fastapi import FastAPI
from routes.product import product

app = FastAPI(
    title="Nissou API",
    description="Simple API made with FastAPI with MongoDB",
    version="1.0.0"
)

app.include_router(product)