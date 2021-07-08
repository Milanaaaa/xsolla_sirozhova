import requests

api_root = 'http://localhost:5000/api/'

print(requests.get(api_root + 'products').json())

# фильтрация по цене
print(requests.get(api_root + 'products', json={'cost': '150'}).json())

# фильтрация по типу
print(requests.get(api_root + 'products', json={'type': 'посуда'}).json())

# фильтрация по цене и типу
print(requests.get(api_root + 'products', json={'cost': '150', 'type': 'посуда'}).json())

# фильтрация по имени
print(requests.get(api_root + 'products', json={'name': 'ложка'}).json())

# фильтрация по scu
print(requests.get(api_root + 'products', json={'scu': '12345678'}).json())

# фильтрация по несуществующему параметру
print(requests.get(api_root + 'products', json={'wrong_param': 'wrong'}).json())
