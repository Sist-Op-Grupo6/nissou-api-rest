from pydantic import BaseModel

class Publication(BaseModel):
    author: str
    date: str
    product: str
    publicationTXT: str
    likes: int