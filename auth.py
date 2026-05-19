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
    expire = datetime.now(timezone.utc) + timedelta(minutes=1)
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

        user_id = payload.get("sub")
        print(datetime.fromtimestamp(payload.get("exp"), tz=timezone.utc))
        
        user_id = int(user_id)
    except ExpiredSignatureError:
        return {"TOken expired"}

    except JWTError:
        return {"Invalid Token"}
    
    user = db.query(models.User).filter(
        models.User.id == user_id
    ).first()

    if user is None:
        return {"Wrong username of password"}
    
    return user