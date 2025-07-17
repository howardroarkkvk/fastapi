from fastapi import FastAPI
from pydantic import BaseModel

app=FastAPI()

class Input(BaseModel):
    name:str
    price:float
    is_available:bool=True

items=[]
@app.post('/greet/')
def greet(input:Input):
    items.append(input)
    return {'name':input.name,
            'price':input.price,
            'is_available':input.is_available}


@app.get('/greet/')
def get_msg():
    return f'returned response is:{items}'


