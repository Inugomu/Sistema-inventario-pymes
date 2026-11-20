from peewee import AutoField, CharField, IntegerField, SQL
from datos.modelos.base import BaseModel
from auxiliares.datos_inventario import defecto

class Almacen(BaseModel):
    id_almacen = AutoField()
    nombre_almacen = CharField(max_length=100)
    direccion = CharField(max_length=150, null=True)
    capacidad_maxima = IntegerField(null=True, constraints=[SQL(defecto)])

    class Meta:
        table_name = 'almacen'


