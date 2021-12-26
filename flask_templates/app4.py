# Formularios con FlaskForm
from flask import Flask, render_template, session, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import (StringField, BooleanField, DateTimeField, RadioField, SelectField, TextAreaField, SubmitField )

from wtforms.validators import DataRequired# para poner campos obligatorios


app = Flask(__name__)
app.config['SECRET_KEY'] = "miclavesecreta"

class formulario(FlaskForm):# creo una clase formulario la cual hereda de el paquete FlaskForm, defino los atributos de la clase
  nombre =  StringField('Nombre', validators=[DataRequired()])# para que los datos simpre se llenen
  edad =  BooleanField('Eres mayor de edad')
  sexo = RadioField('sexo', choices=[('hombre', 'hombre'), ('mujer', 'mujer')]) # 1.nombre->valor interno...2.nombre->lo que vera el usuario 
  color = SelectField('Color Favorito', choices=[('r','rojo'), ('v','verde'),('a','amarillo')])
  comentario = TextAreaField()
  boton =  SubmitField('Enviar')
  

@app.route('/datos', methods=['GET', 'POST'])
def datos():
  miformulario = formulario()
  if miformulario.validate_on_submit():# si el formulario ya fue enviado
    session['nombre'] = miformulario.nombre.data
    session['edad'] = miformulario.edad.data
    session['sexo'] = miformulario.sexo.data
    session['color'] = miformulario.color.data
    session['comentario'] = miformulario.comentario.data
    # guardar en seccion todos los datos del formulario dentro de toda la aplicacion para luego ser recuperados 
    return redirect(url_for('informacion'))#redirecciona a una ruta mediante la funcion de la direccion
  # si el formulario y los datos no fieron enviados...entonces me redireccionara a lapagina datos donde esta el formulario
  return render_template('datos.html', formulario=miformulario)

@app.route('/informacion')
def informacion():
  return render_template('informacion.html')



if __name__ =='__main__':
  app.run(debug=True)
  