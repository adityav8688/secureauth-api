from fastapi import FastAPI
from database import Base, engine
from user import router
import models

app = FastAPI()

app.include_router(router)

@app.on_event("startup")
def on_startup():
    Base.metadata.create_all(bind=engine)

@app.get("/")
def root():
    return {"message":"Backend is running."}