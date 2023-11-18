from pydantic import BaseModel
from models.user import User
from models.product import Product
from models.comments import Comments
from schemas.user import userEntity
from schemas.product import productEntity

class PublicationDB(BaseModel):
    id: str
    author: User
    date: str
    product: Product
    publicationTXT: str
    likes: int
    comments: list

def publicationEntity(item)->dict:
    return{
        "id": str(item["_id"]),
        "author": userEntity(item["author"]),
        "date": item["date"],
        "product": productEntity(item["product"]),
        "publicationTXT": item["publicationTXT"],
        "likes": item["likes"],
        "comments": item["comments"]
    }

def publicationListEntity(entity) -> list:
    return [publicationEntity(item) for item in entity]

