from peewee import AutoField, CharField, IntegerField, DateField, SQL
from datos.model_base import ModelBase

defecto_habilitado = "DEFAULT 1"

class Usuario(ModelBase):
    id_usuario = AutoField()
    rut = CharField(max_length=12, unique=True)
    nombre = CharField(max_length=50)
    apellido = CharField(max_length=50)
    correo = CharField(max_length=191, unique=True)
    password = CharField(max_length=60)
    rol = CharField(max_length=30, default='OPERADOR')
    fecha_incorporacion = DateField()
    habilitado = IntegerField(constraints=[SQL(defecto_habilitado)])

    class Meta:
        table_name = 'usuario'