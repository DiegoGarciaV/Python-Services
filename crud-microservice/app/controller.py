from flask import Blueprint, render_template
import requests
import json

views_controller = Blueprint('controller', __name__)

@views_controller.route('/')
def home():
    return render_template('index.html')

@views_controller.route('/maze-solver')
def maze_solver():
    external_endpoint = 'https://dinobotica.mx:8443/Portafolio/api/ia/search/maze/ass'  # Reemplaza con tu URL externa

    data_to_send = {
        "unaccessibleNodes": [],
        "rootNode": [0,0],
        "targetNode":  [9,9],
        "mazeSize": 10
    }

    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }

    # Convierte los datos a formato JSON
    json_data = json.dumps(data_to_send)

    response = requests.post(external_endpoint, data=json_data, headers=headers)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        return {'message': 'Error al obtener datos externos'}, 500