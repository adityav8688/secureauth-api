from fastapi import APIRouter, Depends, HTTPException, Query, Path, Body
from database import get_db
import schemas, models
from sqlalchemy.orm import Session
from typing import Annotated


item_router = APIRouter(prefix="/items")

@item_router.post("/")
def add_item(item: schemas.itemInfo, db: Session=Depends(get_db)):
    item_info = models.Item(
        name = item.name,
        price = item.price
    )
    db.add(item_info)
    db.commit()
    db.refresh(item_info)
    return item

@item_router.get("/",response_model=list[schemas.itemInfo])
def get_items(db: Session=Depends(get_db)):
    items = db.query(models.Item).all()
    return items

@item_router.post("/some")
def prac(item: schemas.itemInfo, q: Annotated[str|None, Body()]=None):
    return {"message":q, "item":item}