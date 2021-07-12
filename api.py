import flask
from flask import jsonify, request
from flask_restful import Api

from data import db_session
from data.products import Products

blueprint = flask.Blueprint(
    'products_api',
    __name__
)
api = Api(blueprint)


# создание товара
@blueprint.route('/api/product', methods=['POST'])
def create_product():
    print('add')
    if not request.json:
        return jsonify({'error': 'Empty request'})
    elif not all(key in request.json for key in
                 ['scu', 'name', 'type', 'cost']):
        return jsonify({'error': 'Bad request'})

    db_sess = db_session.create_session()
    products = db_sess.query(Products).all()
    products_scu = [p.scu for p in products]
    if request.json['scu'] in products_scu:
        return jsonify({'error': 'Duplicate scu'})

    index_list = [p.id for p in products if p is not None]
    maximum = max(index_list)
    new_id = min([i for i in range(1, maximum + 1) if i not in index_list])

    product = Products(
        id=new_id,
        scu=request.json['scu'],
        name=request.json['name'],
        type=request.json['type'],
        cost=request.json['cost']
    )
    db_sess.add(product)
    db_sess.commit()
    return jsonify({'id': product.id})


# редактирование товара по его идентификатору или SKU
@blueprint.route('/api/product/<int:n>', methods=['PUT'])
def edit_product(n):
    db_sess = db_session.create_session()
    if not request.json:
        return jsonify({'error': 'Empty requests'})

    if len(str(n)) != 8:
        product = db_sess.query(Products).filter(Products.id == n).first()
        if not product:
            return jsonify({'error': 'Invalid id'})

    else:
        product = db_sess.query(Products).filter(Products.scu == n).first()
        if not product:
            return jsonify({'error': 'Invalid scu'})

    id_new, scu_new, name_new, type_new, cost_new = product.id, product.scu, product.name, product.type, product.cost

    products = db_sess.query(Products).all()
    products_scu = [p.scu for p in products]

    if request.json is not None:
        if 'scu' in request.json:
            scu_new = request.json['scu']
        if 'name' in request.json:
            name_new = request.json['name']
        if 'type' in request.json:
            type_new = request.json['type']
        if 'cost' in request.json:
            cost_new = request.json['cost']

    if scu_new in products_scu:
        return jsonify({'error': 'Duplicate scu'})

    db_sess.delete(product)
    db_sess.commit()

    product_new = Products(
        id=id_new,
        scu=scu_new,
        name=name_new,
        type=type_new,
        cost=cost_new
    )
    db_sess.add(product_new)
    db_sess.commit()
    return jsonify({'success': 'OK'})


# удаление товара по его идентификатору или SKU
@blueprint.route('/api/product/<int:n>', methods=['DELETE'])
def delete_product(n):
    db_sess = db_session.create_session()
    if len(str(n)) != 8:
        product = db_sess.query(Products).filter(Products.id == n).all()
    else:
        product = db_sess.query(Products).filter(Products.scu == n).all()
    if not product:
        return jsonify({'error': 'Not found'})
    for p in product:
        db_sess.delete(p)
        db_sess.commit()
    return jsonify({'success': 'OK'})


# получение информации о товаре по его идентификатору или SKU
@blueprint.route('/api/product/<int:n>', methods=['GET'])
def get_one_product(n):
    db_sess = db_session.create_session()
    if len(str(n)) != 8:
        product = db_sess.query(Products).filter(Products.id == n).all()
    else:
        product = db_sess.query(Products).filter(Products.scu == n).all()

    final_dict = {}
    for p in product:
        final_dict[p.id] = p.to_dict(only=('id', 'scu', 'name', 'type', 'cost'))

    return jsonify(
        final_dict
    )


def div_list(lst, n):
    for i in range(0, len(lst), n):
        piece = lst[i: n + i]
        if len(piece) < n:
            piece = piece
        yield piece


# получение каталога товаров
@blueprint.route('/api/products', methods=['GET'])
def get_list_products():
    print('lst')
    if request.json is not None:
        if 'scu' in request.json:
            cond_scu = Products.scu == request.json['scu']
        else:
            cond_scu = True

        if 'name' in request.json:
            cond_name = Products.name == request.json['name']
        else:
            cond_name = True

        if 'type' in request.json:
            cond_type = Products.type == request.json['type']
        else:
            cond_type = True

        if 'cost' in request.json:
            cond_cost = Products.cost == request.json['cost']
        else:
            cond_cost = True

        db_sess = db_session.create_session()
        products = db_sess.query(Products).filter(cond_scu, cond_name, cond_type, cond_cost).order_by(Products.id).all()
    else:
        db_sess = db_session.create_session()
        products = db_sess.query(Products).order_by(Products.id).all()

    full_list_prod = {
        'products':
            [item.to_dict(only=('id', 'scu', 'name', 'type', 'cost'))
             for item in products]
    }

    final_list = list(div_list(full_list_prod['products'], 10))

    return jsonify({'data': final_list})
