from fastapi import APIRouter, Response, status
from config.db import conn
from schemas.comment import commentEntity, commentListEntity
from models.comment import Comment
from bson import ObjectId
from starlette.status import HTTP_204_NO_CONTENT

comment = APIRouter()


@comment.get("/comments", response_model=list[Comment], tags=["Comments"])
def find_all_comments():
    return commentListEntity(conn.NissouDB.comments.find())


@comment.get("/comments/{id}", response_model=Comment, tags=["Comments"])
def find_comment_by_id(id: str):
    return commentEntity(conn.NissouDB.comments.find_one({"_id": ObjectId(id)}))

@comment.post("/comments", response_model=Comment, tags=["Comments"])
def create_comment(userId: str, publicationId: str, comment: Comment):
    user = conn.NissouDB.users.find_one({"_id": ObjectId(userId)})
    comment.author = user
    comment.publicationId = publicationId  # Asigna el publicationId al comentario

    new_comment = dict(comment)
    del new_comment["id"]

    id = conn.NissouDB.comments.insert_one(new_comment).inserted_id
    comment = conn.NissouDB.comments.find_one({"_id": id})
    return commentEntity(comment)

@comment.put("/comments/{id}", response_model=Comment, tags=["Comments"])
def update_comment(id: str, Comment: Comment):
    conn.NissouDB.comments.find_one_and_update(
        {"_id": ObjectId(id)}, {"$set": dict(Comment)}
    )
    return commentEntity(conn.NissouDB.comments.find_one({"_id": ObjectId(id)}))


@comment.delete(
    "/comments/{id}", status_code=status.HTTP_204_NO_CONTENT, tags=["Comments"]
)
def delete_comment(id: str):
    commentEntity(conn.NissouDB.comments.find_one_and_delete({"_id": ObjectId(id)}))
    return Response(status_code=HTTP_204_NO_CONTENT)

@comment.get("/comments/publication/{id}", response_model=list[Comment], tags=["Comments"])
def find_comment_by_publicationId(id: str):
    return commentListEntity(conn.NissouDB.comments.find({"publicationId": id}))