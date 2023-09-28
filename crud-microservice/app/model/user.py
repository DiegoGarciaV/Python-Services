from app.h2 import db
 
class User(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(30), nullable=False)
    edad = db.Column(db.Integer, nullable=False)
    locacion = db.Column(db.String(40), nullable=False)