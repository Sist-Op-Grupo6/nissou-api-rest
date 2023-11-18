from typing import Optional
from pydantic import BaseModel

class Product(BaseModel):
    id: str
    name: str
    description: str
    price: float
    image: Optional[str]
    weight: float
    material: str
    quantity: int