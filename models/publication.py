from pydantic import BaseModel

class Publication(BaseModel):
    author: str
    date: str