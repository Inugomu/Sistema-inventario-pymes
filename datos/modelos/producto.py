from peewee import AutoField, CharField, DecimalField, IntegerField, SQL
from datos.modelos.base import BaseModel
from auxiliares.datos_inventario import defecto

class Producto(BaseModel):
    id_producto = AutoField()
    nombre = CharField(max_length=100)
    descripcion = CharField(max_length=255, null=True)
    precio = DecimalField(max_digits=10, decimal_places=2)
    stock_actual = IntegerField(constraints=[SQL(defecto)])
    stock_minimo = IntegerField(constraints=[SQL(defecto)])
    tipo_producto = CharField(max_length=50, null=True)
    id_categoria = IntegerField()
    id_proveedor = IntegerField()

    class Meta:
        table_name = 'producto'  