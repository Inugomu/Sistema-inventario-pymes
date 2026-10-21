from peewee import AutoField, IntegerField, SQL
from datos.modelos.base import BaseModel
from auxiliares.datos_inventario import defecto

class ProductoAlmacen(BaseModel):
    id_registro = AutoField()
    id_producto = IntegerField()
    id_almacen = IntegerField()
    cantidad = IntegerField(constraints=[SQL(defecto)])

    class Meta:
        table_name = 'producto_almacen'