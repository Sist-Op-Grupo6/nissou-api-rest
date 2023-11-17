from fastapi import APIRouter, Response, status
from config.db import conn
from schemas.publication import publicationEntity, publicationListEntity,PublicationDB
from models.publication import Publication
from bson import ObjectId
from starlette.status import HTTP_204_NO_CONTENT

publication = APIRouter()

@publication.get("/publications", response_model=list[PublicationDB], tags=["Publications"])
def find_all_publications():
    return publicationListEntity(conn.NissouDB.publications.find())

@publication.get("/publications/{id}", response_model=PublicationDB, tags=["Publications"])
def find_publication_by_id(id: str):
    return publicationEntity(conn.NissouDB.publications.find_one({"_id": ObjectId(id)}))

@publication.post("/publications", response_model=PublicationDB, tags=["Publications"])
def create_publication(publication: Publication):
    
    user = conn.NissouDB.users.find_one({"_id": ObjectId(publication.author)})
    publication.author = user

    new_pub = dict(publication)

    id = conn.NissouDB.publications.insert_one(new_pub).inserted_id
    publication = conn.NissouDB.publications.find_one({"_id": id})
    
    return publicationEntity(publication)

#@publication.put("/publications/{id}", response_model=PublicationDB, tags=["Publications"])
#def update_publication(id: str, publication: PublicationDB):
#    conn.NissouDB.publications.find_one_and_update(
#        {"_id": ObjectId(id)}, {"$set": dict(publication)}
#    )
#
#    return publicationEntity(conn.NissouDB.publications.find_one({"_id": ObjectId(id)}))

@publication.delete("/publications/{id}", status_code=status.HTTP_204_NO_CONTENT, tags=["Publications"])
def delete_publication(id: str):
    publicationEntity(conn.NissouDB.publications.find_one_and_delete({"_id": ObjectId(id)}))
    return Response(status_code=HTTP_204_NO_CONTENT)