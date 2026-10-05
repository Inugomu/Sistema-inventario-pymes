from peewee import CharField, AutoField, Model, Database, IntegerField
from datos.conexion import conectar

base_datos = conectar()

class BaseModel(Model):
    class Meta:
        database = base_datos
        
class Categoria(BaseModel):
    id_categoria = AutoField()
    nombre_categoria = CharField(max_length=100)

    class Meta:
        table_name = 'categoria'
