from werkzeug.security import generate_password_hash, check_password_hash

password = 'clavesecreta2'
password_encryptada = generate_password_hash(password)
print(password_encryptada)

verificar = check_password_hash(password_encryptada, "clave2")
print(verificar)