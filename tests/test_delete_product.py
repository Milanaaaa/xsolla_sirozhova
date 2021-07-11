import requests
from data.api_root import api_root

# по id
print(requests.delete(api_root + 'product/3').json())

# по scu (удаляются все с таким scu)
print(requests.delete(api_root + 'product/11111111').json())

# переданы ненужные данные
print(requests.delete(api_root + 'product/8', json={'scu': 11111111, 'name': 'кружка', 'cost': '50'}).json())

# по некорректному id
print(requests.delete(api_root + 'product/9').json())

# по некорректному scu
print(requests.delete(api_root + 'product/98765432').json())
