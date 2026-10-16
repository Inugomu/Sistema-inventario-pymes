from peewee import AutoField, DateField, IntegerField, Model
from datos.conexion import conectar

base_datos = conectar()

class BaseModel(Model):
    class Meta:
        database = base_datos

class ProductoPerecible(BaseModel):
    id_perecible = AutoField()
    id_producto = IntegerField()  # O ForeignKeyField(Producto, ...)
    fecha_vencimiento = DateField()

    class Meta:
        table_name = 'producto_perecible'