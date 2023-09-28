from flask import request, jsonify, Blueprint, current_app
from flask_mysqldb import MySQL
from app import database
from app import h2

users_api = Blueprint('api', __name__)

@users_api.route('/', methods=['POST'])
def create():
    data = request.get_json()
    name = data['nombre']
    age = data['edad']
    location = data['locacion']

    cur = database.mysql.connection.cursor()
    cur.execute("INSERT INTO usuarios (nombre, edad,locacion) VALUES (%s, %s, %s)", (name, age,location))
    database.mysql.connection.commit()
    cur.close()

    return {'message': 'Item creado correctamente'}, 201


@users_api.route('/<int:user_id>', methods=['GET'])
def get(user_id):
    cur = database.mysql.connection.cursor()
    cur.execute("SELECT * FROM usuarios WHERE id = %s", (user_id,))
    item = cur.fetchone()
    cur.close()
    if item:
        return {'id': item[0], 'nombre': item[1], 'edad': item[2], 'locacion': item[3]}
    else:
        return {'message': 'Item no encontrado'}, 404

@users_api.route('/', methods=['GET'])
def getall():
    cur = database.mysql.connection.cursor()
    cur.execute("SELECT * FROM usuarios")
    users = cur.fetchall()
    users_list = []
    cur.close()
    for item in users:
        item_dict =  {'id': item[0], 'nombre': item[1], 'edad': item[2], 'locacion': item[3]}
        users_list.append(item_dict)
    
    return jsonify(users_list)
    
@users_api.route('/<int:user_id>', methods=['PUT'])
def update(user_id):
    data = request.get_json()
    name = data['nombre']
    age = data['edad']
    location = data['locacion']

    cur = database.mysql.connection.cursor()
    cur.execute("UPDATE usuarios SET nombre = %s, edad = %s, locacion = %s WHERE id = %s", (name, age, location, user_id))
    database.mysql.connection.commit()
    cur.close()
    return {'message': 'Item actualizado correctamente'}

@users_api.route('/<int:user_id>', methods=['DELETE'])
def delete(user_id):

    cur = database.mysql.connection.cursor()
    cur.execute("DELETE FROM usuarios WHERE id = %s", (user_id,))
    database.mysql.connection.commit()
    cur.close()

    return {'message': 'Item eliminado correctamente'}, 201
