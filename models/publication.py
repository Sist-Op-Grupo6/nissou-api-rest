from pydantic import BaseModel
from models.user import User
from models.product import Product

class Publication(BaseModel):
    id: str
    author: User
    date: str
    product: Product
    title: str
    description: str
    likes: int