import requests

api_root = 'http://localhost:5000/api/'

# по id
print(requests.get(api_root + 'product/1').json())

# по scu (информация обо всех товарах с таким scu)
print(requests.get(api_root + 'product/12345678').json())

# переданы ненужные данные
print(requests.get(api_root + 'product/8', json={'scu': 11111111, 'name': 'кружка', 'cost': '50'}).json())

# по некорректному id
print(requests.get(api_root + 'product/9').json())

# по некорректному scu
print(requests.get(api_root + 'product/98765432').json())
