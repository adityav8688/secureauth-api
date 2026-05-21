from fastapi import FastAPI
from database import Base, engine
from routers.user import user_router
from routers.items import item_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost:5173",  
    "http://127.0.0.1:5173",
]

app.include_router(user_router)
app.include_router(item_router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# class Item(BaseModel):
#     name: Annotated[str, Query(min_length=3, max_length=15)]
#     discription: Annotated[str|None , Query(max_length=200)]
#     price: float
#     tax: Annotated[float | None, Query()]

@app.on_event("startup")
def on_startup():
    Base.metadata.create_all(bind=engine)

@app.get("/")
def root():
    return {"message":"it is updating even now"}

# @app.post("/items/")
# def read_items(item: itemInfo):
#     item_dict = item.model_dump()
#     if item.tax != 0:
#         total = item.price + item.tax
#         item_dict.update({"total":total})
#     return item_dict

# @app.post("/items")
# def create_items(item: itemInfo):
#     pass