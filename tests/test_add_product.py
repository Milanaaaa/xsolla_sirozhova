import requests
from data.api_root import api_root

# корректные данные
print(requests.post(api_root + 'product',
                    json={'scu': 13106111, 'name': 'тарелка', 'type': 'посуда', 'cost': '50'}).json())

# нет типа
print(requests.post(api_root + 'product', json={'scu': 11111111, 'name': 'кружка', 'cost': '50'}).json())

# цена типа int
print(
    requests.post(api_root + 'product', json={'scu': 11111451, 'name': 'кружка', 'type': 'посуда', 'cost': 100}).json())

# имя типа int
print(requests.post(api_root + 'product', json={'scu': 11251111, 'name': 123, 'type': 'посуда', 'cost': '50'}).json())
