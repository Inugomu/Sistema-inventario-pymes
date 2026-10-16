from peewee import AutoField, IntegerField, Model
from datos.conexion import conectar

base_datos = conectar()

class BaseModel(Model):
    class Meta:
        database = base_datos

class ProductoAlmacen(BaseModel):
    id_registro = AutoField()
    id_producto = IntegerField()  # O ForeignKeyField(Producto, ...)
    id_almacen = IntegerField()   # O ForeignKeyField(Almacen, ...)
    cantidad = IntegerField(default=0)

    class Meta:
        table_name = 'producto_almacen'