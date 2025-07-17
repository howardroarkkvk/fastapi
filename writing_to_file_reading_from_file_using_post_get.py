from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
import json
import os

class Item(BaseModel):
    name:str
    price:float
    is_available:bool=True

app=FastAPI()

data_file='items.json'

def fetch_items():
    if not os.path.exists(data_file):
        return []
    with open(data_file,'r') as f:
        data=json.load(f)
        return [Item(**item) for item in data] # this unpacks the data in to list of dictionaries present in data variable(i.e loaded from json file) like [{"name": "Apple", "price": 10.0, "is_available": true}, {"name": "Banana", "price": 5.0, "is_available": false}]

def save_items(items:List[Item]):
    with open(data_file,'w') as f:
        json.dump([item for item in items],f,indent=2) #.model_dump()


@app.post('/items/')
def post_item(item:Item):
    items=fetch_items()
    items.append(item)
    save_items(items)
    return {'message':"items saved",'item':item}

@app.get('/items/')
def get_item():
    items=fetch_items()
    return {'items':items}





    
