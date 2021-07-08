import requests

api_root = 'http://localhost:5000/api/'

# добавляем товар
print(requests.post(api_root + 'product',
                    json={'scu': 11111115, 'name': 'стол', 'type': 'мебель', 'cost': '550'}).json())

# получаем информацию о нём по id, полученному в прошлом тесте
print(requests.get(api_root + 'product/9').json())  # product/{id}

# меняем scu и имя
print(requests.put(api_root + 'product/3',
                   json={'scu': 12345678, 'name': 'шкаф'}).json())

# получаем информацию о нём по новому scu
print(requests.get(api_root + 'product/12345678').json())

# получаем список товаров с таким же scu
print(requests.get(api_root + 'products', json={'scu': '12345678'}).json())

# удаляем товар по id
print(requests.delete(api_root + 'product/9').json())
