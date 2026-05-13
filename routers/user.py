from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
import models, schemas
from securities import hash_password, verify_password
from auth import create_token

user_router = APIRouter(prefix="/auth", tags=["Auth"])

@user_router.post("/register")
def register(user: schemas.userCreate, db: Session=Depends(get_db)):
    existing = db.query(models.User).filter(models.User.email == user.email).first()
    if existing or "":
        raise HTTPException(status_code=400, detail="Email already registered")
    
    new_user = models.User(
        email = user.email,
        password = hash_password(user.password)
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return {"message": "user created "+new_user.email}

@user_router.post("/login")
def login(user: schemas.userCreate, db: Session=Depends(get_db)):
    ex_user = db.query(models.User).filter(models.User.email == user.email).first()

    if not ex_user or not (verify_password(user.password, ex_user.password)):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    
    token = create_token({"sub": ex_user.email})

    return {
        "access_token": token,
        "token_type": "bearer"
    }