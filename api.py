import flask
from flask import jsonify, request

from data import db_session
from data.products import Products

blueprint = flask.Blueprint(
    'products_api',
    __name__
)


# создание товара
@blueprint.route('/api/product', methods=['POST'])
def create_product():
    if not request.json:
        return jsonify({'error': 'Empty request'})
    elif not all(key in request.json for key in
                 ['scu', 'name', 'type', 'cost']):
        return jsonify({'error': 'Bad request'})
    db_sess = db_session.create_session()
    product = Products(
        scu=request.json['scu'],
        name=request.json['name'],
        type=request.json['type'],
        cost=request.json['cost']
    )
    db_sess.add(product)
    db_sess.commit()
    return product.id


# редактирование товара
@blueprint.route('/api/product/<int:id>', methods=['POST', 'GET'])
def edit_product(id):
    db_sess = db_session.create_session()
    if not request.json:
        return jsonify({'error': 'Empty requests'})
    if request.method == 'GET':
        product = db_sess.query(Products).get(id)
        if not product:
            return jsonify({'products': {}, 'error': 'Not found'})
        return jsonify({'products': product.to_dict(only=('scu', 'name', 'type', 'cost'))})
    elif request.method == 'POST':
        product = db_sess.query(Products).get(id)
        if id != request.json['id']:
            return jsonify({'products': {}, 'error': 'Bad request'})
        if not product:
            return jsonify({'products': {}, 'error': 'Invalid id'})
        product.id = request.json['id']
        product.scu = request.json['scu'],
        product.name = request.json['name'],
        product.type = request.json['type'],
        product.cost = request.json['cost']
        db_sess.merge(product)
        db_sess.commit()
        return jsonify({'result': 'OK'})


# удаление товара
@blueprint.route('/api/product/<int:id>', methods=['DELETE'])
def delete_product(id):
    db_sess = db_session.create_session()
    product = db_sess.query(Products).get(id)
    if not product:
        return jsonify({'error': 'Not found'})
    db_sess.delete(product)
    db_sess.commit()
    return jsonify({'success': 'OK'})


# получение информации о товаре по его идентификатору или SKU
@blueprint.route('/api/product/<int:id>', methods=['GET'])
def get_one_product(id):
    db_sess = db_session.create_session()
    product = db_sess.query(Products).get(id)
    if not product:
        return jsonify({'error': 'Not found'})
    return jsonify(
        {
            'products': product.to_dict(only=('id', 'scu', 'name', 'type', 'cost'))
        }
    )


# получение каталога товаров
@blueprint.route('/api/product')
def get_products():
    db_sess = db_session.create_session()
    products = db_sess.query(Products).all()
    full_list_prod = {
            'products':
                [item.to_dict(only=('id', 'scu', 'name', 'type', 'cost'))
                 for item in products]
        }
    print(type(full_list_prod))
    return jsonify(
        {
            'products':
                [item.to_dict(only=('id', 'scu', 'name', 'type', 'cost'))
                 for item in products]
        }
    )
