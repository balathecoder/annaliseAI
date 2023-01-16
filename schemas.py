from pydantic import BaseModel

class Image(BaseModel):
    file_path: str
    tags: str
    user_id: int

class User(BaseModel):
    name: str
    email: str
    password: str

class Login(BaseModel):
    username: str
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str


