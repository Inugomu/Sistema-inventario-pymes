from peewee import IntegerField
from datos.model_base import ModelBase

class EntradaInventario(ModelBase):
    id_movimiento = IntegerField(primary_key=True)
    id_proveedor = IntegerField()

    class Meta:
        table_name = 'entrada_inventario'