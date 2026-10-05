from peewee import AutoField, Database, IntegerField, IntergerField, Model, CharField, Database, Model
from datos.conexion import conectar
from auxiliares.datos_inventario import defecto

base_datos = conectar()

class BaseModel(Model):
    class Meta:
        database = base_datos

class Almacen(BaseModel):
    id_almacen = AutoField()
    nombre_almacen = CharField(max_length=100)
    direccion = CharField(max_length=150, null=True)
    capacidad_maxima = IntegerField(null=True, default=defecto)

    class Meta:
        table_name = 'almacen'


