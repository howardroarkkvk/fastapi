from fastapi import FastAPI,status
from pydantic import BaseModel


class Item(BaseModel):
    name:str
    price:float
    is_available:bool=True



app=FastAPI()

# get from endpoint # status_code=status.HTTP_200_OK
@app.get("/greet")
def get(name:str='Guest'):
    return {"message":f"Hello {name} , Welcome to Fast API"}

# post to endpoint
@app.post("/greet/")
def create_item(item:Item):
    return {'message':"Item Received","item_detials":item}


