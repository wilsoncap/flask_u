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