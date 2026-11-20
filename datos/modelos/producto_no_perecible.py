from peewee import IntegerField, SQL
from datos.modelos.base import BaseModel
from auxiliares.datos_inventario import defecto

class ProductoNoPerecible(BaseModel):
    id_producto = IntegerField(primary_key=True)
    garantia_meses = IntegerField(constraints=[SQL(defecto)])

    class Meta:
        table_name = 'producto_no_perecible'