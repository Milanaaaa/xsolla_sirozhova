import requests
api_root = 'http://localhost:5000/api/'

# создание товара
print(requests.post(api_root + 'product', json={'scu': 11111111, 'name': 'тарелка', 'type': 'посуда', 'cost': '50'}).json())


# print()
# print(requests.get('http://127.0.0.1:5000//api/product/1').json())
# print()
# print(requests.delete('http://127.0.0.1:5000//api/product/1').json())
# print()
# print(requests.get('http://127.0.0.1:5000/api/product/12345678').json())
# print()
# print(requests.get('http://127.0.0.1:5000/api/products', json={'cost': '150'}).json())


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
