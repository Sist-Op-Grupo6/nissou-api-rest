from schemas.user import userEntity
from schemas.product import productEntity

def publicationEntity(item) -> dict:
    return {
        "id": str(item["_id"]),
        "author": userEntity(item["author"]),
        "date": item["date"],
        "product": productEntity(item["product"]),
        "title": item["title"],
        "description": item["description"],
        "likes": item["likes"],
        "comments": item["comments"],
    }
    
def publicationListEntity(entity) -> list:
    return [publicationEntity(item) for item in entity]
