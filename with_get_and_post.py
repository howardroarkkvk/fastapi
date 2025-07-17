from fastapi import FastAPI
from pydantic import BaseModel
from typing import List


class Item(BaseModel):
    name:str
    price:float
    is_available:bool=True

items_db:List[Item]=[]
app=FastAPI()

@app.post("/items/")
def create_item(item:Item):
    items_db.append(item)
    return {'message': 'Items added successfully','item':item}



@app.get("/items/")
def get_all_items():
    return {'items':items_db}