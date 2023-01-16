from datetime import datetime, timedelta
from jose import JWTError, jwt
from typing import Optional
from annaliseAI import schemas

SECRET_KEY='464d150eb35bd4a89a3aebab8222191b894ac87b6da71d31799c5411f77c7c2f'
ALGORITHM='HS256'
ACCESS_TOKEN_EXPIRE_MINTES=30

def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow()+expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINTES)
    to_encode.update({'exp':expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

def verify_token(token: str, credentials_exception):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email: str = payload.get('sub')
        if email is None:
            raise credentials_exception
        token_data = schemas.TokenData(email=email)
    except JWTError:
        raise credentials_exception