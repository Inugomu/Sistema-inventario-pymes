from peewee import DateField, IntegerField
from datos.modelos.base import BaseModel

class ProductoPerecible(BaseModel):
    id_producto = IntegerField(primary_key=True)
    fecha_vencimiento = DateField()

    class Meta:
        table_name = 'producto_perecible'