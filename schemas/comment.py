from schemas.user import userEntity


def commentEntity(item) -> dict:
    return {
        "id": str(item["_id"]),
        "author": userEntity(item["author"]),
        "date": item["date"],
        "text": item["text"],
    }


def commentListEntity(entity) -> list:
    return [commentEntity(item) for item in entity]