from peewee import AutoField, CharField
from datos.modelos.base import BaseModel

class Proveedor(BaseModel):
    id_proveedor = AutoField()
    nombre = CharField(max_length=100)
    telefono = CharField(max_length=20, null=True)
    email = CharField(max_length=100, null=True)

    class Meta:
        table_name = 'proveedor'