import requests

api_root = 'http://localhost:5000/api/'

print(requests.get(api_root + 'products').json())

print(requests.get(api_root + 'products', json={'cost': '150'}).json())

print(requests.get(api_root + 'products', json={'type': 'посуда'}).json())

print(requests.get(api_root + 'products', json={'cost': '150', 'type': 'посуда'}).json())
