from typing import Optional
from pydantic import BaseModel

class User(BaseModel):
    first_name: str
    last_name: str
    email : str
    password : str
    age: int
    gender: str