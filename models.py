from sqlalchemy import Column, Integer, String,DateTime, Float
from database import Base
from datetime import datetime

class User(Base):
    __tablename__ = "users"

    id = Column("id",Integer, primary_key=True, index=True)
    email = Column("email",String, unique=True, index=True)
    password = Column("password",String, nullable=False)
    timestamp = Column("timestamp",DateTime, default= datetime.now())

class Item(Base):
    __tablename__ = "items"

    id = Column("item_id",Integer, primary_key=True, index=True)
    name = Column("name",String, nullable=False)
    price = Column("price",Float, nullable=False)
    