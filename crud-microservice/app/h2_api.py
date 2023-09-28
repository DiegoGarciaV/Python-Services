from flask import request, jsonify, Blueprint
from app.h2 import db
from app.model.user import User

users_api = Blueprint('api_h2', __name__)

none_user = "Usuario no encontrado"

@users_api.route('/', methods=['POST'])
def create():
    data = request.get_json()
    name = data['nombre']
    age = data['edad']
    location = data['locacion']

    new_user = User(nombre=name,edad=age,locacion=location)
    db.session.add(new_user)
    db.session.commit()
    return {'message': 'Usuario creado correctamente'}, 201


@users_api.route('/<int:user_id>', methods=['GET'])
def get(user_id):
    
    user = User.query.get(user_id) 

    if user:
        return {'id': user.id, 'nombre': user.nombre, 'edad': user.edad, 'locacion': user.locacion}
    else:
        return {'message': none_user}, 404

@users_api.route('/', methods=['GET'])
def getall():
    users = User.query.all()
    users_list = [{'id': user.id, 'nombre': user.nombre, 'edad': user.edad, 'locacion': user.locacion} for user in users]
    return jsonify(users_list)
    
@users_api.route('/<int:user_id>', methods=['PUT'])
def update(user_id):
    data = request.get_json()
    name = data['nombre']
    age = data['edad']
    location = data['locacion']

    user = User.query.get(user_id)

    if user is None:
        return jsonify(message=none_user), 404
    
    user.nombre = name
    user.edad = age
    user.locacion = location
    db.session.commit()

    return {'message': 'Usuario actualizado correctamente'}

@users_api.route('/<int:user_id>', methods=['DELETE'])
def delete(user_id):

    user = User.query.get(user_id)

    if user is None:
        return jsonify(message=none_user), 404
    
    db.session.delete(user)
    db.session.commit()

    return {'message': 'Usuario eliminado correctamente'}, 201
