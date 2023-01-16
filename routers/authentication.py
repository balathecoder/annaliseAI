from datetime import timedelta
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from annaliseAI import schemas, database, models
from annaliseAI.JWT_token import ACCESS_TOKEN_EXPIRE_MINTES, create_access_token
from annaliseAI.hashing import *
from fastapi.security import OAuth2PasswordRequestForm

auth_router = APIRouter(
    tags = ['authentication']
)

@auth_router.post('/login')
def login(request: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(database.get_db)):
    user = db.query(models.User).filter(models.User.email == request.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
        detail='Incorrect password'
        )
    
    access_token = create_access_token(
        data = ('sub':user.email),
    )

    return {'access_token': access_token, 'token_type': 'bearer'}