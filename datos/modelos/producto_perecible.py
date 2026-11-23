from peewee import DateField, IntegerField
from datos.model_base import ModelBase

class ProductoPerecible(ModelBase):
    id_producto = IntegerField(primary_key=True)
    fecha_vencimiento = DateField()

    class Meta:
        table_name = 'producto_perecible'