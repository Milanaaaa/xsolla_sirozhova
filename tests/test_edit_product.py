import requests
from data.api_root import api_root

# по id
print(requests.put(api_root + 'product/11',
                   json={'scu': 11112131, 'name': 'нож', 'cost': '150'}).json())

# по scu
print(requests.put(api_root + 'product/11111112',
                   json={'scu': 11111112, 'name': 'вилка', 'cost': '50'}).json())

# по некорректному id
print(requests.put(api_root + 'product/9',
                   json={'scu': 11111111, 'name': 'ложка', 'cost': '150'}).json())

# по некорректному scu
print(requests.put(api_root + 'product/98765432',
                   json={'scu': 11111111, 'name': 'ложка', 'cost': '150'}).json())
