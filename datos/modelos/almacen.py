from peewee import AutoField, CharField, IntegerField, SQL
from datos.model_base import ModelBase
from auxiliares.datos_inventario import defecto

defecto_habilitado = "DEFAULT 1"

class Almacen(ModelBase):
    id_almacen = AutoField()
    nombre_almacen = CharField(max_length=100)
    direccion = CharField(max_length=150, null=True)
    capacidad_maxima = IntegerField(null=True, constraints=[SQL(defecto)])
    habilitado = IntegerField(constraints=[SQL(defecto_habilitado)])

    class Meta:
        table_name = 'almacen'