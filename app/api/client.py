from flask import jsonify, request, url_for
from app.api import api
from app.models.tables import Client, db


@api.route('/client', methods=['GET'], defaults={'id': None})
@api.route('/client/<int:id>', methods=['GET'])
def get_client(id):
    if id is not None:
        product = Client.query.get_or_404(id)
        return jsonify(product.to_json())
    else:
        clients = Client.query.all()
        response = jsonify({'clients': [client.to_json() for client in clients]})
        response.status_code = 200
        return response


@api.route('/client/<int:id>/address', methods=['GET'])
def get_client_address(id):
    client = Client.query.get_or_404(id)
    address = client.address
    return jsonify(address.to_json())


@api.route('/client', methods=['POST'])
def create_client():
    client = Client.from_json(request.json)
    db.session.add(client)
    db.session.commit()
    return jsonify(client.to_json()), 201, {'Location': url_for('api.get_client', id=client.id, _external=True)}


@api.route('/client/<int:id>', methods=['PUT'])
def edit_client(id):
    client = Client.query.get_or_404(id)
    client.name = request.json.get('name')
    client.phone_number = request.json.get('phone_number')
    client.notifiable = request.json.get('notifiable')
    client.status = request.json.get('notifiable')

    db.session.add(client)
    db.session.commit()
    return jsonify(client.to_json()), 200, {'Location': url_for('api.get_product', id=client.id, _external=True)}


@api.route('/client/<int:id>/address', methods=['PUT'])
def edit_address(id):
    client = Client.query.get_or_404(id)

    client.address.street = request.json.get('street')
    client.address.detail = request.json.get('detail')
    client.address.zip_code = request.json.get('zip_code')

    db.session.add(client)
    db.session.commit()
    return jsonify(client.to_json()), 200, {'Location': url_for('api.get_product', id=client.id, _external=True)}