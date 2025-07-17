import requests

url='http://127.0.0.1:8000/greet/'

item_data={"name":'Pencil Apple',
           'price':46500,
           'is_available':True}

response=requests.post(url,json=item_data)
print("status  code:",response.status_code)
print("Response  Json:",response.json())