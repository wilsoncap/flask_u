from sqlalchemy.sql.schema import PrimaryKeyConstraint
from app6 import basededatos, Persona

#-- metodo de insercion
basededatos.create_all()

persona1 = Persona('antonio', 39)
persona2 = Persona('juan', 27)

basededatos.session.add_all([persona1, persona2])# agregar las dos personas a la DB
basededatos.session.commit()# para confirmar los cambios guardados en la DB


persona3 = Persona('maria', 25)#instancio el objeto con los parametros a ingresar
basededatos.session.add(persona3)# recupero esos datos que quedaron guardados en la instancia y se lo inyecto a la base de datos
basededatos.session.commit()# commit para confirmar desde la DB

#---Crando consultas

personas = Persona.query.all()
print('consultar todas las personas')
print(personas)

filtro1 = Persona.query.filter_by(nombre="antonio")
print('filtro por nombre * Antonio')
print(filtro1.all())

selecion1 = Persona.query.get(2)
print("busqueda por id")
print(selecion1)

#--metodo actualizar
persona = Persona.query.get(1)
persona.edad = 45
basededatos.session.add(persona)
basededatos.session.commit()


#--metodo eliminar
persona_borrar = Persona.query.get(3)
basededatos.session.delete(persona_borrar)
basededatos.session.commit()
print('Hemos borrado esta persona {}'.format(persona_borrar))

personasall = Persona.query.all()
print('todas las personas')
print(personasall)