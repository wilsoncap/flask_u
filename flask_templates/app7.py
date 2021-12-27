from flask_bcrypt import Bcrypt

generador = Bcrypt()
password = "clavesecreta"
password_encriptada = generador.generate_password_hash(password)
print(password_encriptada)


verificar = generador.check_password_hash(password_encriptada, 'clavesecreta')
print(verificar)