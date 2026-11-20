from peewee import IntegerField
from datos.modelos.base import BaseModel

class EntradaInventario(BaseModel):
    id_movimiento = IntegerField(primary_key=True)
    id_proveedor = IntegerField()

    class Meta:
        table_name = 'entrada_inventario'