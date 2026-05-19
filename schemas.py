from pydantic import BaseModel, EmailStr, Field
from datetime import datetime

class userInfo(BaseModel):
    email: EmailStr
    password: str
    timestamp: datetime

class userCreate(BaseModel):
    email: EmailStr
    password: str = Field(max_length=100)

class itemInfo(BaseModel):
    name: str
    price: float
