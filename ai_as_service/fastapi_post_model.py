from fastapi import FastAPI,Request
from pydantic import BaseModel
import numpy as np
import pickle
import os

app=FastAPI()

path=r'D:\DataFiles\ai_as_service'
result=None
class IrisInput(BaseModel):
    input_features:list[float]

with open(os.path.join(path,'iris_model.pkl'),'rb') as f:
    model=pickle.load(f)


@app.post('/predict/')
def predict(input:IrisInput,request:Request):
    x=np.array(input.input_features).reshape(1,-1)
    result=int(model.predict(x)[0])
    request.app.state.last_prediction=result
    return {'prediction':result}


@app.get('/predict/')
def get_item(request:Request):
    if hasattr(request.app.state,"last_prediction"):
        return {'response':request.app.state.last_prediction}
    return {'response':'No prediction made yet'}

