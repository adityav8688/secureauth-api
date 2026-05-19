from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from database import get_db
import models, schemas
from securities import hash_password, verify_password
from auth import create_token, get_current_user

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
def login(user: OAuth2PasswordRequestForm = Depends(), db: Session=Depends(get_db)):
    ex_user = db.query(models.User).filter(models.User.email == user.username).first()

    if not ex_user or not (verify_password(user.password, ex_user.password)):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    
    token = create_token({"sub": str(ex_user.id)})

    return {
        "access_token": token,
        "token_type": "bearer"
    }

@user_router.get("/users", response_model=list[schemas.userInfo])
def users(db: Session = Depends(get_db)):
    users = db.query(models.User).all()
    return users

@user_router.get("/user")
def current_user(user: models.User = Depends(get_current_user)):
    return user