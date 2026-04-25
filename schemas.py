from pydantic import BaseModel, EmailStr
from datetime import datetime

class userInfo(BaseModel):
    email: EmailStr
    password: str
    timestamp: datetime

class userCreate(BaseModel):
    email: EmailStr
    password: str