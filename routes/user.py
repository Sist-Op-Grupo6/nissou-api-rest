from fastapi import APIRouter, Response, status
from config.db import conn
from schemas.user import userEntity, userListEntity
from models.user import User
from bson import ObjectId
from starlette.status import HTTP_204_NO_CONTENT

user = APIRouter()

@user.get("/users", response_model=list[User], tags=["Users"])
def find_all_users():
    return userListEntity(conn.NissouDB.users.find())


@user.get("/users/{id}", response_model=User, tags=["Users"])
def find_user_by_id(id: str):
    return userEntity(conn.NissouDB.users.find_one({"_id": ObjectId(id)}))


@user.get("/users/{email}/{password}", response_model=User, tags=["Users"])
def find_user_by_email_password(email: str, password: str):
    return userEntity(conn.NissouDB.users.find_one({"email": email, "password": password}))


@user.post("/users", response_model=User, tags=["Users"])
def create_user(user: User):
    new_user = dict(user)
    id = conn.NissouDB.users.insert_one(new_user).inserted_id
    user = conn.NissouDB.users.find_one({"_id": id})
    return userEntity(user)


@user.put("/users/{id}", response_model=User, tags=["Users"])
def update_user(id: str, user: User):
    conn.NissouDB.users.find_one_and_update(
        {"_id": ObjectId(id)}, {"$set": dict(user)}
    )

   ## Actualiza el nombre del usuario en todas las publicaciones
   #conn.NissouDB.publications.update_many(
   #    {"author._id": ObjectId(user_id)},
   #    {"$set": {"author.name": new_name}}
   #)

    return userEntity(conn.NissouDB.users.find_one({"_id": ObjectId(id)}))


@user.delete(
    "/users/{id}", status_code=status.HTTP_204_NO_CONTENT, tags=["Users"]
)
def delete_user(id: str):
    userEntity(conn.NissouDB.users.find_one_and_delete({"_id": ObjectId(id)}))
    return Response(status_code=HTTP_204_NO_CONTENT)