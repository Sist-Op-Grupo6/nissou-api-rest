from typing import Optional
from datetime import date
from pydantic import BaseModel

class Comments(BaseModel):
    id: str
    authorName: str
    date: str  # Use datetime.date
    commentText: str
