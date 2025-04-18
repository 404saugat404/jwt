from fastapi import FastAPI, Depends, HTTPException, Query
from models import Document
from db import documents_db, users_db

app=FastAPI()

def get_user(username:str=Query(...)):
    user=users_db.get(username)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user
 

@app.get("/documents", response_model=list[Document])
def get_documents(user=Depends(get_user)):
    filtered_documents=[i for i in documents_db if i.department==user.department]
    return filtered_documents

@app.get("/documents/{doc_id}", response_model=Document)
def get_document(doc_id:int, user=Depends(get_user)):
    document=next((doc for doc in documents_db if doc.id==doc_id and doc.department==user.department), None)
    if not document:
        raise HTTPException(status_code=404, detail="Document not found or access denied")
    return document


