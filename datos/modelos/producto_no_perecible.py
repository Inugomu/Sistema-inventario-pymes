from peewee import IntegerField, SQL
from datos.model_base import ModelBase
from auxiliares.datos_inventario import defecto

class ProductoNoPerecible(ModelBase):
    id_producto = IntegerField(primary_key=True)
    garantia_meses = IntegerField(constraints=[SQL(defecto)])

    class Meta:
        table_name = 'producto_no_perecible'