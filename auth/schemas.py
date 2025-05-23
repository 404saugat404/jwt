from pydantic import BaseModel

class TokenData(BaseModel):
    username: str
    role: str

class Token(BaseModel):
    access_token: str
    token_type: str