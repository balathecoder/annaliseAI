from sqlalchemy.orm import Session
from annaliseAI import models
from annaliseAI import schemas
from fastapi import HTTPException, status

def show(id: int, db: Session):
    image = db.query(models.Image).filter(models.Image.id == id).first()
    if not image:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'{id} not found')
    return image

def create(request: schemas.Image, db: Session):
    