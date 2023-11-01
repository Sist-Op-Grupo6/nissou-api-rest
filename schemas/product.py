def productEntity(item) -> dict:
    return {
        "id": item["id"],
        "name": item["name"],
        "description": item["description"],
        "price": item["price"],
        "image": item["image"],
        "weight": item["weight"],
        "material": item["material"]
    }


def productListEntity(entity) -> list:
    return [productEntity(item) for item in entity]