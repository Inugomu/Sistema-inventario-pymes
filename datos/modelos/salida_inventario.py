from peewee import AutoField, CharField, IntegerField, Model
from datos.conexion import conectar

base_datos = conectar()

class BaseModel(Model):
    class Meta:
        database = base_datos

class SalidaInventario(BaseModel):
    id_salida = AutoField() 
    id_movimiento = IntegerField()  
    motivo_salida = CharField(max_length=255)

    class Meta:
        table_name = 'salida_inventario'