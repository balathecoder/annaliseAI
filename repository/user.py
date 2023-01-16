from sqlalchemy.orm import Session
from annaliseAI import models, schemas, hashing
from fastapi import HTTPException, status

def create(request: schemas.User, db: Session):
    new_user = models.User(name=request.name, email=request.email, password=hashing.hash.bcrypt(request.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def get(id, db):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
        details='user {id} not found'
        )
    return user