import requests

api_root = 'http://localhost:5000/api/'

# по id
print(requests.put(api_root + 'product/3',
                    json={'scu': 11111111, 'name': 'ложка', 'cost': '150'}).json())

print(requests.put(api_root + 'product/11111111',
                    json={'scu': 11111112, 'name': 'вилка', 'cost': '150'}).json())
