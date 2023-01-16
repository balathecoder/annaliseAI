from fastapi import Depends, HTTPException, status
from annaliseAI import JWT_token
from fastapi.security import OAuth2PasswordBearer
## for authentication
auth2_scheme = OAuth2PasswordBearer(tokenUrl='login')

def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail='Could not validate credentials',
        headers={'WWW-Authenticate','Bearer'},
    )
    return JWT_token.verify_token(token, credentials_exception)