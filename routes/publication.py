from fastapi import APIRouter, Response, status
from config.db import conn
from schemas.publication import publicationEntity, publicationListEntity
from models.publication import Publication
from bson import ObjectId
from starlette.status import HTTP_204_NO_CONTENT

publication = APIRouter()


@publication.get(
    "/publications", response_model=list[Publication], tags=["Publications"]
)
def find_all_publications():
    return publicationListEntity(conn.NissouDB.publications.find())


@publication.get(
    "/publications/{id}", response_model=Publication, tags=["Publications"]
)
def find_publication_by_id(id: str):
    return publicationEntity(conn.NissouDB.publications.find_one({"_id": ObjectId(id)}))

@publication.get("/publications/user/{user_id}", response_model=list[Publication], tags=["Publications"])
def find_publications_by_user(user_id: str):
    user_publications = conn.NissouDB.publications.find({"author._id": ObjectId(user_id)})
    return publicationListEntity(user_publications)


@publication.post("/publications", response_model=Publication, tags=["Publications"])
def create_publication(userId: str, productId: str, publication: Publication):
    user = conn.NissouDB.users.find_one({"_id": ObjectId(userId)})
    publication.author = user

    product = conn.NissouDB.products.find_one({"_id": ObjectId(productId)})
    publication.product = product
    
    new_pub = dict(publication)

    id = conn.NissouDB.publications.insert_one(new_pub).inserted_id
    publication = conn.NissouDB.publications.find_one({"_id": id})

    return publicationEntity(publication)


@publication.put(
    "/publications/{id}", response_model=Publication, tags=["Publications"]
)
def update_publication(id: str, new_title: str, new_description: str):
    conn.NissouDB.publications.update_one(
        {"_id": ObjectId(id)}, {"$set": {"title": new_title}}
    )
    return publicationEntity(conn.NissouDB.publications.find_one({"_id": ObjectId(id)}))


@publication.delete(
    "/publications/{id}", status_code=status.HTTP_204_NO_CONTENT, tags=["Publications"]
)
def delete_publication(id: str):
    publicationEntity(
        conn.NissouDB.publications.find_one_and_delete({"_id": ObjectId(id)})
    )
    return Response(status_code=HTTP_204_NO_CONTENT)
