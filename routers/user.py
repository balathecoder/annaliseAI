from fastapi import FastAPI, status, HTTPException, Response, Depends, APIRouter
from annaliseAI import schemas, database, models, hashing, oauth2
from sqlalchemy.orm import Session
from typing import List
from annaliseAI.repository import user

user_router = APIRouter(
    prefix='/user',
    tags=['users']
)

def verify_password(plain_password, hashed_password):
    return hashing.pwd_context.verify(plain_password, hashed_password)

def get_password(password):
    return hashing.pwd_context.hash(password)

@user_router.post('/',response_model=schemas.ShowUser)
def create_user(request: schemas.User, db: Session = Depends(database.get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return user.get(id, db)