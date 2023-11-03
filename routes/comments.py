from fastapi import APIRouter, Response, status
from config.db import conn
from schemas.comments import commentEntity, commentListEntity
from models.comments import Comments
from bson import ObjectId
from starlette.status import HTTP_204_NO_CONTENT

comments = APIRouter()

@comments.get("/comments",response_model=list[Comments], tags=["Comments"])
def find_all_comments():
  return commentListEntity(conn.NissouDB.comments.find())

@comments.get("/comments/{id}", response_model=Comments, tags=["Comments"])
def find_comment_by_id(id: str):
    return commentEntity(conn.NissouDB.comments.find_one({"_id": ObjectId(id)}))


@comments.post("/comments", response_model=Comments, tags=["Comments"])
def create_comment(comments: Comments):
    new_comment = dict(comments)
    id = conn.NissouDB.comments.insert_one(new_comment).inserted_id
    comments = conn.NissouDB.comments.find_one({"_id": id})
    return commentEntity(comments)


@comments.put("/comments/{id}", response_model=Comments, tags=["Comments"])
def update_comment(id: str, comments: Comments):
    conn.NissouDB.comments.find_one_and_update(
        {"_id": ObjectId(id)}, {"$set": dict(comments)}
    )
    return commentEntity(conn.NissouDB.comments.find_one({"_id": ObjectId(id)}))


@comments.delete(
    "/comments/{id}", status_code=status.HTTP_204_NO_CONTENT, tags=["Comments"]
)
def delete_comment(id: str):
    commentEntity(conn.NissouDB.comments.find_one_and_delete({"_id": ObjectId(id)}))
    return Response(status_code=HTTP_204_NO_CONTENT)
