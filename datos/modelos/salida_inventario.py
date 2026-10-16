from peewee import AutoField, CharField, IntegerField, Model
from datos.conexion import conectar

base_datos = conectar()

class BaseModel(Model):
    class Meta:
        database = base_datos

class SalidaInventario(BaseModel):
    id_salida = AutoField()  # O id_movimiento según tu esquema de BD
    id_movimiento = IntegerField()  # O ForeignKeyField(MovimientoInventario, ...)
    motivo_salida = CharField(max_length=255)

    class Meta:
        table_name = 'salida_inventario'