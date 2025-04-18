from pydantic import BaseModel
from typing import List

class User(BaseModel):
    username: str
    department: str


class Document(BaseModel):
    id: int
    title: str
    content: str
    department: str

    