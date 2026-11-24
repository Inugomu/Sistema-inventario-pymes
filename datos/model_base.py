from peewee import Model
from datos.conexion import conectar

base_datos = conectar()

class ModelBase(Model):
    class Meta:
        database = base_datos