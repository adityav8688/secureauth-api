from jose import jwt, JWTError
from jose.exceptions import ExpiredSignatureError
from datetime import datetime, timedelta, timezone
from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session

from oauth2 import oauth2_scheme
from database import get_db
import models

SECRET_KEY = "lAZYai_seCRET_HASh_3000"
ALGORITHM = "HS256"

def create_token(data: dict):
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + timedelta(hours=2)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)


def get_current_user(
        token: str = Depends(oauth2_scheme),
        db : Session = Depends(get_db)
    ):

    print(token)
    try:
        payload = jwt.decode(
            token,
            SECRET_KEY,
            algorithms=[ALGORITHM]
        )
    except ExpiredSignatureError:
        raise HTTPException(
            status_code=401,
            detail="token expired"
        )

    except JWTError:
        raise HTTPException(
            status_code=401,
            detail="invalid token"
        )
    
    user_id = payload.get("sub")        

    if user_id is None:
        raise HTTPException(
            status_code=401,
            detail="Invalid token"
        )
        
    user_id = int(user_id)
    
    user = db.query(models.User).filter(
        models.User.id == user_id
    ).first()

    if user is None:
        raise HTTPException(
            status_code=401,
            detail="user not found"
        )
    
    return user