from typing import Optional
from datetime import date
from pydantic import BaseModel
from models.user import User

class Comment(BaseModel):
    id: str
    author: User
    publicationId : str
    date: str  # Use datetime.date
    text: str
