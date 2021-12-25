import re
from flask import Flask, render_template, request
from flask.wrappers import Request

app = Flask(__name__)

@app.route("/")
def index():
  return "<h2>probando plantillas</h2>"

@app.route("/pagina1")
def pagina1():
  return render_template("pagina1.html")

@app.route("/pagina2")
def pagina2():
  return render_template("pagina2.html")

@app.route("/formulario")
def formulario():
  return render_template("formulario.html")

@app.route("/gracias")
def gracias():
  var1 = request.args.get('nombre')
  var2 = request.args.get('apellidos')
  return render_template("gracias.html", nombre = var1, apellidos = var2)


@app.route("/nombre")
def nombre():
  return render_template("nombre.html")

@app.route("/resultado")
def resultado():
  nombre = request.args.get('nombre')
  minuscula = any(letra.islower() for letra in nombre)
  numero = any(letra.isdigit() for letra in nombre)
  mayuscula = nombre[0].isupper()
  todo = minuscula and numero and mayuscula
  return render_template("resultado.html", todo=todo, minuscula=minuscula, mayuscula=mayuscula, numero=numero)

@app.errorhandler(404)
def pagina_no_encontrada(e):
  return render_template('pagina404.html'), 404





  

if __name__ =='__main__':
  app.run(debug=True)
  
  




# crear entirno virtua: virtualenv -p python3 env
# para activar ese entorno virtual: .\env\Scripts\Activate
# para instalar paquetes: pip install flask flask_mysqldb
# para levantar un servidor: python src/app.py
# para habilitar el cosumo de una api: pip install flask-cors

# py -m pip install virtualenv  --> para crear entorno virtual globalmente
# Virtualenv -p python3 env, otro_nombre  --> para crear entorno virtual localmente
# pip list -->para ver lo que hay en la ruta actual
# pip install flask --> para insalar flask
# .\env\Scripts\Activate --> para entrar al entorno virual donde podemos instalar paquetes, librerias y framework
# deactivate --> para salir del entorno virtual
# pip freeze > requirements.txt --> crea un archivo con todos los paquetes del proyecto para que se puedan migrar a otro proyecto
# pip install -r requirements.txt --> para instalar los paquetes en otro proyecto
# python .\app\app.py --> se ejecuta en el entorno virtual
# python.exe pip install --upgrade pip
# python .\app\app.py --> para levantar el servidor
# python .\src\app.py
# pip list --outdated --> para ver los paquetes que estan desactualizados
# pip show "nombre del paquete" --> para ver toda la informacion mas detallada del paquete
# pip check "nombre del paquete" --> sirve para ver si el paquete tiene algun faltante de otra dependencia o estas esten rotas
# pip install flask-sqlalchemy --> modulo para comunicarse con base de datos
# pip install flask-marshmallow --> modulo para definir squemas en nuestra base de datos
# pip install marshmallow-sqlalchemy --> librerias que trabajan entre ellas mismas
# pip install pymysql -->modulo para poder crear conexion con la base de datos