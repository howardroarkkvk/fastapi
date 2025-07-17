import requests

url='http://127.0.0.1:8000/predict/'

data={'input_features':[0.45,0.6,0.7,0.8]}

response=requests.post(url,json=data)
print(response.json())