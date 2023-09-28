from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app.api import users_api
from app.h2_api import users_api as users_api_h2
from app.controller import views_controller
from app import database
from app import h2
from app.model.user import User

app = Flask(__name__)
app.config.from_pyfile('h2_db.py')
app.config.from_pyfile('mysql.py')
database.mysql.init_app(app)
h2.db.init_app(app)
with app.app_context():
    h2.db.create_all()

app.jinja_options = {'variable_start_string': '{{{', 'variable_end_string': '}}}'}

# Registrar la API y el controlador en la aplicación
app.register_blueprint(users_api, url_prefix='/api/users')
app.register_blueprint(users_api_h2, url_prefix='/api/h2/users')
app.register_blueprint(views_controller)

if __name__ == '__main__':
    app.run(
        port=8008
    )
