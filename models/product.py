from typing import Optional
from pydantic import BaseModel

class Product(BaseModel):
    id: int
    name: str
    description: str
    price: float
    image: Optional[str]
    weight: float
    material: str