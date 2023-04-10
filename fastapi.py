from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

from utilis import postgretopython

app = FastAPI()
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Item(BaseModel):
    item_id:int
    name: str
    price: float
    discription: str
    category: str
    is_offer: Union[bool, None] = None


@app.get("/")
def read_root():
    return {"Hello": "Raushan"}


@app.get("/items/{item_id}")
def read_item(item_id: str, q: Union[str, None] = None, p: str='Raushan'):
    return {"item_id": item_id, "q": q, "p":p}


@app.post("/items")
def save_item(item: Item):
    postgretopython.drop_table_if_not_exist()
    print(item)
    #save to database
    return {"item":item}


@app.put("/items")
def save_item(item: Item):

    print(item)
    #update  to database
    return {"item":item}
