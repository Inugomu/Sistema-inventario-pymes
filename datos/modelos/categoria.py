from peewee import AutoField, CharField
from datos.modelos.base import BaseModel

class Categoria(BaseModel):
    id_categoria = AutoField()
    nombre_categoria = CharField(max_length=100)

    class Meta:
        table_name = 'categoria'