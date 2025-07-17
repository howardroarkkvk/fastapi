import pickle
from sklearn.linear_model import LogisticRegression
from sklearn.datasets import load_iris
import os

path=r'D:\DataFiles\ai_as_service'

X,y=load_iris(return_X_y=True)
# print(X,X.shape)
# print(y,y.shape)

model=LogisticRegression()
model.fit(X,y)

with open(os.path.join(path,'iris_model.pkl'),'wb') as f:
    pickle.dump(model,f) # dump is to write to the file....