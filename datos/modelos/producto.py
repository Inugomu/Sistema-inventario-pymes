from peewee import AutoField, CharField, DecimalField, IntegerField, Model
from datos.conexion import conectar

base_datos = conectar()

class BaseModel(Model):
    class Meta:
        database = base_datos

class Producto(BaseModel):
    id_producto = AutoField()
    nombre = CharField(max_length=100)
    descripcion = CharField(max_length=255, null=True)
    precio = DecimalField(max_digits=10, decimal_places=2)
    stock_actual = IntegerField(default=0)
    stock_minimo = IntegerField(default=0)
    tipo_producto = CharField(max_length=50, null=True)
    id_categoria = IntegerField()  # O ForeignKeyField(Categoria, ...) si usas relaciones
    id_proveedor = IntegerField()  # O ForeignKeyField(Proveedor, ...) si usas relaciones

    class Meta:
        table_name = 'producto'