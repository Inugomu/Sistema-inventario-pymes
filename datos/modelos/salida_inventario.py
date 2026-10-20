from peewee import CharField, IntegerField
from datos.modelos.base import BaseModel

class SalidaInventario(BaseModel):
    id_movimiento = IntegerField(primary_key=True)
    motivo_salida = CharField(max_length=150, null=True)

    class Meta:
        table_name = 'salida_inventario'