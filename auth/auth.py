from datetime import datetime, timedelta
from auth.schemas import Token, TokenData
from jose import jwt, JWTError
from config import SECRET_KEY, ALGORITHM

def create_access_token(data:dict , expires_delta:timedelta=None):
    to_encode = data.copy()
    expire=datetime.utcnow() + expires_delta
    to_encode.update({'exp': expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

def decode_access_token(token:str)->TokenData:
    payload= jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    username:str=payload.get('sub')
    role:str=payload.get('role')
    if username is None or role is None:
        raise JWTError('username or role not found')
    return TokenData(username=username, role=role)