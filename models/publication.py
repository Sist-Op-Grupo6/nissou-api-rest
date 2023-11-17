from pydantic import BaseModel
from models.comments import Comments
from typing import Optional

class Publication(BaseModel):
    author: str
    date: str
    product: str
    publicationTXT: str
    likes: int
    comments: Optional[list[Comments]]