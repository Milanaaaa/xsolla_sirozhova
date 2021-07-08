import requests

api_root = 'http://localhost:5000/api/'

# по id
print(requests.put(api_root + 'product/3',
                   json={'scu': 11111111, 'name': 'ложка', 'cost': '150'}).json())

# по scu
print(requests.put(api_root + 'product/11111112',
                   json={'scu': 11111112, 'name': 'вилка', 'cost': '50'}).json())

# по некорректному id
print(requests.put(api_root + 'product/9',
                   json={'scu': 11111111, 'name': 'ложка', 'cost': '150'}).json())

# по некорректному scu
print(requests.put(api_root + 'product/98765432',
                   json={'scu': 11111111, 'name': 'ложка', 'cost': '150'}).json())
