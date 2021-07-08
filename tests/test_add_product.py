import requests

api_root = 'http://localhost:5000/api/'

# корректные данные
print(requests.post(api_root + 'product',
                    json={'scu': 11111111, 'name': 'тарелка', 'type': 'посуда', 'cost': '50'}).json())

# нет типа
print(requests.post(api_root + 'product', json={'scu': 11111111, 'name': 'кружка', 'cost': '50'}).json())

# цена типа int
print(
    requests.post(api_root + 'product', json={'scu': 11111111, 'name': 'кружка', 'type': 'посуда', 'cost': 100}).json())

# имя типа int
print(requests.post(api_root + 'product', json={'scu': 11111111, 'name': 123, 'type': 'посуда', 'cost': '50'}).json())
