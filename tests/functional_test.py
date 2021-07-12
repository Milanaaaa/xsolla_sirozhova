import requests
from data.api_root import api_root

# добавляем товар
print(requests.post(api_root + 'product',
                    json={'scu': 11131115, 'name': 'стол', 'type': 'мебель', 'cost': '550'}).json())

# получаем информацию о нём по id, полученному в прошлом тесте
print(requests.get(api_root + 'product/20').json())  # product/{id}

# меняем scu и имя
print(requests.put(api_root + 'product/20',
                   json={'scu': 12345600, 'name': 'шкаф'}).json())

# получаем информацию о нём по новому scu
print(requests.get(api_root + 'product/12345600').json())

# получаем список товаров с таким же type
print(requests.get(api_root + 'products', json={'type': 'мебель'}).json())

# удаляем товар по id
print(requests.delete(api_root + 'product/20').json())
