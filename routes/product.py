from fastapi import APIRouter
from config.db import conn
from schemas.product import productEntity, productListEntity

product = APIRouter()

@product.get("/products")
def find_all_products():
    return productListEntity(conn.local.products)

@product.get("/products/{id}")
def find_product_by_id(id: int):
    return id

@product.post("/products")
def create_product():
    return "create"

@product.put("/products/{id}")
def update_product(id: int):
    return id

@product.delete("/products/{id}")
def delete_product(id: int):
    return id