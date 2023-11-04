from pydantic import BaseModel
from models.user import User
from models.product import Product
from schemas.user import userEntity
from schemas.product import productEntity

class PublicationDB(BaseModel):
    author: User
    date: str
    product: Product
    publicationTXT: str
    likes: int

def publicationEntity(item)->dict:
    return{
        "id": str(item["_id"]),
        "author": userEntity(item["author"]),
        "date": item["date"],
        "product": productEntity(item["product"]),
        "publicationTXT": item["publicationTXT"],
        "likes": item["likes"]
    }

def publicationListEntity(entity) -> list:
    return [publicationEntity(item) for item in entity]
