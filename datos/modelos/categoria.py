from peewee import AutoField, CharField
from datos.model_base import ModelBase

class Categoria(ModelBase):
    id_categoria = AutoField()
    nombre_categoria = CharField(max_length=100)

    class Meta:
        table_name = 'categoria'