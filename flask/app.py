from flask import Flask

app = Flask(__name__)

@app.route("/")
def principal():
  return "<h1>Hola mundo</h1>"

@app.route("/adios")
def adios():
  return "<h2>Adios de de flask</h2>"

@app.route("/cama/<nombre>")
def cama(nombre):
  return "<h2>hola {}, te saludaos desde flask</h2>".format(nombre)

@app.route("/longitud/<nombre>")
def longitud(nombre):
  valor = len(nombre)
  return "<h2>hola {}, tu longitud de nombr es {}</h2>".format(nombre, valor)

@app.route("/edad/<nombre>/<edad>")
def edad(nombre, edad):
  return "<h2>hola {}, tu edad es {}</h2>".format(nombre, edad)

@app.route("/sumar/<int:n1>/<int:n2>")
def sumar(n1, n2):
  suma =  n1 + n2
  return "<h2>la suma de {}, y  {} da como resulatdo {}</h2>".format(n1, n2, suma)


if __name__ =='__main__':
  app.run(debug=True)
  
  




# crear entirno virtua: virtualenv -p python3 env
# para activar ese entorno virtual: .\env\Scripts\Activate
# para instalar paquetes: pip install flask flask_mysqldb
# para levantar un servidor: python src/app.py
# para habilitar el cosumo de una api: pip install flask-cors