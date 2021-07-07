import requests

api_root = 'http://localhost:5000/api/'

# по id
print(requests.delete(api_root + 'product/3').json())

# по scu
print(requests.delete(api_root + 'product/11111111').json())
