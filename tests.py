import requests
api_root = 'http://localhost:5000/api/'

print(requests.get('http://localhost:5000/api/product').json())
# # Получение всех работ
# print(requests.get(api_root + 'product').json())
#
# # Корректное получение одной работы
# print(requests.get(api_root + 'jobs/1').json())
#
# # Ошибочны запрос на получение одной работы - неверный id
# print(requests.get(api_root + 'jobs/12').json())
#
# # Ошибочны запрос на получение одной работы - строка
# print(requests.get(api_root + 'jobs/one').json())
