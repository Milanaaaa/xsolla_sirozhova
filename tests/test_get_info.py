import requests
api_root = 'http://localhost:5000/api/'

# по id
print(requests.get(api_root + 'product/1').json())

# по scu
print(requests.get(api_root + 'product/11111111').json())