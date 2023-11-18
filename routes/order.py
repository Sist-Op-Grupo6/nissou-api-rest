from fastapi import APIRouter, Response, status
from config.db import conn
from schemas.order import orderEntity, orderListEntity
from models.orders import Order
from bson import ObjectId
from starlette.status import HTTP_204_NO_CONTENT

orders = APIRouter()

@orders.get("/orders",response_model=list[Order], tags=["Orders"])
def find_all_comments():
  return orderListEntity(conn.NissouDB.orders.find())

@orders.get("/orders/{id}", response_model=Order, tags=["Orders"])
def find_comment_by_id(id: str):
    return orderEntity(conn.NissouDB.orders.find_one({"_id": ObjectId(id)}))

@orders.post("/orders", response_model=Order, tags=["Orders"])
def create_comment(orders: Order):
    new_order = dict(orders)
    id = conn.NissouDB.orders.insert_one(new_order).inserted_id
    orders = conn.NissouDB.orders.find_one({"_id": id})
    return orderEntity(orders)

@orders.put("/orders/{id}", response_model=Order, tags=["Orders"])
def update_order(id: str, order: Order):
    conn.NissouDB.orders.find_one_and_update(
        {"_id": ObjectId(id)}, {"$set": dict(order)}
    )
    return orderEntity(conn.NissouDB.orders.find_one({"_id": ObjectId(id)}))

@orders.delete(
    "/orders/{id}", status_code=status.HTTP_204_NO_CONTENT, tags=["Orders"]
)
def delete_order(id: str):
    orderEntity(conn.NissouDB.orders.find_one_and_delete({"_id": ObjectId(id)}))
    return Response(status_code=HTTP_204_NO_CONTENT)
