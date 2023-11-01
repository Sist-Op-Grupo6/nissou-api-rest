def userEntity(item) -> dict:
    return {
        "id": str(item["_id"]),
        "first_name": item["first_name"],
        "last_name": item["last_name"],
        "age": item["age"],
        "gender": item["gender"],
    }


def userListEntity(entity) -> list:
    return [userEntity(item) for item in entity]