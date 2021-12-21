from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def portada():
  diccionario = {'nombre':'Wilson', 'edad':34, 'carrera': 'ing sistemas'}
  return render_template("portada.html", datos = diccionario)


# @app.route("/colores")
# def colores():
#   lista = ['verde', 'amarillo','azul', 'morado']
#   return render_template("colores.html", colores = lista)

@app.route("/frase/<texto>")
def colores(texto):
  return render_template("frase.html", tipo = texto)





if __name__ =='__main__':
  app.run(debug=True)
  
  




# crear entirno virtua: virtualenv -p python3 env
# para activar ese entorno virtual: .\env\Scripts\Activate
# para instalar paquetes: pip install flask flask_mysqldb
# para levantar un servidor: python src/app.py
# para habilitar el cosumo de una api: pip install flask-cors