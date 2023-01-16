from fastapi import APIRouter, Depends, status, UploadFile
from sqlalchemy.orm import Session
from annaliseAI import schemas, database
from annaliseAI.repository import image
import os
image_router = APIRouter(
    prefix='/image',
    tags=['image']
)
@image_router.post('/')
def image(image: UploadFile = File(...)):
    print(image.file)
    try:
        os.mkdir('images')
        print(os.getcwd())
    except Exception as e:
        print(e)
    file_name = f'{os.getcwd()}/images/{image.filename.replace(" ","-")}'
    with open(file_name,'wb') as f:
        f.write(image.file.read())
        f.close()
    return {'filename':file_name}
"""
@image_router.get('/{id}',status_code=200)
def show(id, db: Session = Depends(database.get_db)):
    return image.show(id, db)

@image_router.post('/',status_code=status.HTTP_201_CREATED)
def create(request: schemas.Image, db: Session = Depends(database.get_db)):
    return image.create(request, db)

@image_router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
def update(id, request: schemas.Image, db: Session = Depends(database.get_db)):
    return image.update()

@image_router.delete('/{id}',status_code=status.HTTP_204_NO_CONTENT)
def destroy(id: int, db: Session = Depends(database.get_db)):
    return image.destry(id, db)
"""