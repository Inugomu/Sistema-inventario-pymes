from peewee import AutoField, IntegerField, SQL
from datos.model_base import ModelBase
from auxiliares.datos_inventario import defecto

class ProductoAlmacen(ModelBase):
    id_registro = AutoField()
    id_producto = IntegerField()
    id_almacen = IntegerField()
    cantidad = IntegerField(constraints=[SQL(defecto)])

    class Meta:
        table_name = 'producto_almacen'