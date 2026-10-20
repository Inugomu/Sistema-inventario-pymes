from peewee import AutoField, DateField, IntegerField, CharField
from datos.modelos.base import BaseModel

class MovimientoInventario(BaseModel):
    id_movimiento = AutoField()
    fecha = DateField()
    cantidad = IntegerField()
    observacion = CharField(max_length=255, null=True)
    tipo_movimiento = CharField(max_length=20)
    id_producto = IntegerField()

    class Meta:
        table_name = 'movimiento_inventario'