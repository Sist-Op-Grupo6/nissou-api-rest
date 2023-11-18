def commentEntity(item) -> dict:
  return {
    "id": str(item["_id"]),
    "authorName": item["authorName"],
    "date": item["date"],
    "commentText": item["commentText"],
  }

def commentListEntity(entity) -> list:
  return [commentEntity(item) for item in entity]
