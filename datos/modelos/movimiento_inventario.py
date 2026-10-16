from peewee import AutoField, DateTimeField, IntegerField, Model
from datos.conexion import conectar

base_datos = conectar()

class BaseModel(Model):
    class Meta:
        database = base_datos

class MovimientoInventario(BaseModel):
    id_movimiento = AutoField()
    cantidad = IntegerField()
    fecha_movimiento = DateTimeField()
    id_producto = IntegerField()  # O ForeignKeyField(Producto, ...)

    class Meta:
        table_name = 'movimiento_inventario'