import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

directorio = os.path.abspath(os.path.dirname(__file__))


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(directorio, 'datos.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

basededatos = SQLAlchemy(app)

# creacion del modelo de base de datos

class Persona(basededatos.Model):
  __tablename__ = 'Personas'
  
  id = basededatos.Column(basededatos.Integer, primary_key =True)
  nombre = basededatos.Column(basededatos.Text)
  edad = basededatos.Column(basededatos.Integer)
  
  def __init__(self, nombre, edad):
    self.nombre = nombre
    self.edad = edad
  
  def __repr__(self):
      texto = "Personas : nombre={} y edad={}".format(self.nombre, self.edad)
      return texto