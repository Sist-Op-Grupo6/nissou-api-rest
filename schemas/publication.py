from pydantic import BaseModel
from models.user import User
from schemas.user import userEntity

class PublicationDB(BaseModel):
    author: User
    date: str

def publicationEntity(item)->dict:
    return{
        "id": str(item["_id"]),
        "author": userEntity(item["author"]),
        "date": item["date"],

    }

def publicationListEntity(entity) -> list:
    return [publicationEntity(item) for item in entity]

