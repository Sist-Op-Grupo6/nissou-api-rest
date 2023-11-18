from datetime import date
from pydantic import BaseModel

class Order(BaseModel):
    id: str
    order_date: date
    customer_name: str
    product_name: str