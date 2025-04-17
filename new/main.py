from auth import get_current_user
from utils import create_access_token
from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm


app = FastAPI()

fake_users_db = {
    "user_name":"saugat",
    "password":"123456"
}


@app.post("/login")
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    if form_data.username in fake_users_db["user_name"] and form_data.password == fake_users_db["password"]:
        token=create_access_token(data={"sub": form_data.username})
        return {"access_token": token, "token_type": "bearer"}
    return {"msg": "Incorrect username or password"}


@app.get("/protected")
def protected_route(user:dict = Depends(get_current_user)):
    return {"msg": "You are in the protected route", "user": user}