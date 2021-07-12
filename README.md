**Product API - система управления товарами для площадки электронной коммерции**


***Содержание***

_В API присутствуют следующие методы:_
* **Создание товара.** `'/api/product', methods=['POST']` 
Метод генерирует и возвращает уникальный идентификатор товара.

* **Редактирование товара.** `'/api/product/<int:n>', methods=['PUT']` 
Метод изменяет все данные о товаре по его идентификатору или SKU. Есть возможность изменить не все атрибуты.

* **Удаление товара.** `'/api/product/<int:n>', methods=['DELETE']` 
Метод удаляет все данные о товаре по его идентификатору или SKU.

* **Получение информации.** `'/api/product/<int:n>', methods=['GET']` 
Метод предоставляет информацию о товаре по его идентификатору или SKU.

* **Получение каталога товаров.** `'/api/products', methods=['GET']` 
Метод возвращает список всех добавленных товаров из базы данных списками по 10 элементов. 
Возможна фильтрация товаров по scu, имени, типу и стоимости.


Все данные о товарах хранятся в **Базе Данных**, в таблице _Products_ со столбцом для каждого атрибута класса товара.

**Класс товара** `Products` имеет атрибуты:
* **id** (уникальный, не меняется)
* **SCU** (уникальный, может меняться пользователем на еще не занятый)
* **имя** (не уникальный, может меняться пользователем)
* **тип** (не уникальный, может меняться пользователем)
* **стоимость** (не уникальный, может меняться пользователем)


***Как запустить и тестировать API***

_Требуются следующие **библиотеки**:_
* requests
* sqlalchemy
* flask
* flask_restful
* SQLAlchemy-serializer
* sqlalchemy

1. В папке **data**, в файле **api_root.py** найдите переменную port_num. Это номер порта для запуска API. Удостоверьтесь, что он _не занят_ (это можно проверить, введя в командную строку `netstat -a` (Windows), `netstat -pnltu` (Linux)), если нет, то замените на _свободный_.
2. Запустите файл **main.py**.
3. В консоли будет адрес порта (например, http://127.0.0.1:5000/), в папке **data**, в файле **api_root** есть переменная **api_root**, в нее нужно _**вставить адрес порта**_.
4. В папке **tests** находятся тесты для каждого метода и функциональный тест. Запустите любой из них.

Можно самостоятельно написать тесты (имеющиеся взять как пример) и тестировать на них по такому же алгоритму, запуская в шаге №4.

