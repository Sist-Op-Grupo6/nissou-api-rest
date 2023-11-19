from fastapi import APIRouter, Response, status
from config.db import conn
from schemas.product import productEntity, productListEntity
from models.product import Product
from bson import ObjectId
from starlette.status import HTTP_204_NO_CONTENT

product = APIRouter()


@product.get("/products", response_model=list[Product], tags=["Products"])
def find_all_products():
    return productListEntity(conn.NissouDB.products.find())


@product.get("/products/{id}", response_model=Product, tags=["Products"])
def find_product_by_id(id: str):
    return productEntity(conn.NissouDB.products.find_one({"_id": ObjectId(id)}))


@product.post("/products", response_model=Product, tags=["Products"])
def create_product(product: Product):
    new_product = dict(product)
    del new_product["id"]

    id = conn.NissouDB.products.insert_one(new_product).inserted_id
    product = conn.NissouDB.products.find_one({"_id": id})

    return productEntity(product)

@product.put("/products/{id}", response_model=Product, tags=["Products"])
def update_product(id: str, product: Product):
    conn.NissouDB.products.find_one_and_update(
        {"_id": ObjectId(id)}, {"$set": dict(product)}
    )
    return productEntity(conn.NissouDB.products.find_one({"_id": ObjectId(id)}))


@product.delete(
    "/products/{id}", status_code=status.HTTP_204_NO_CONTENT, tags=["Products"]
)
def delete_product(id: str):
    productEntity(conn.NissouDB.products.find_one_and_delete({"_id": ObjectId(id)}))
    return Response(status_code=HTTP_204_NO_CONTENT)
