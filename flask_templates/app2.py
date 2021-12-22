from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
  return "<h2>probando plantillas</h2>"

@app.route("/pagina1")
def pagina1():
  return render_template('pagina1.html')

@app.route("/pagina2")
def pagina2():
  return render_template('pagina2.html')
  

if __name__ =='__main__':
  app.run(debug=True)
  
  




# crear entirno virtua: virtualenv -p python3 env
# para activar ese entorno virtual: .\env\Scripts\Activate
# para instalar paquetes: pip install flask flask_mysqldb
# para levantar un servidor: python src/app.py
# para habilitar el cosumo de una api: pip install flask-cors