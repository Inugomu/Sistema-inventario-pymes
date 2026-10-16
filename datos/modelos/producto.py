from peewee import AutoField, CharField, DecimalField, IntegerField, Model
from datos.conexion import conectar
from auxiliares.datos_inventario import defecto

base_datos = conectar()

class BaseModel(Model):
    class Meta:
        database = base_datos

class Producto(BaseModel):
    id_producto = AutoField()
    nombre = CharField(max_length=100)
    descripcion = CharField(max_length=255, null=True)
    precio = DecimalField(max_digits=10, decimal_places=2)
    stock_actual = IntegerField(defecto)
    stock_minimo = IntegerField(defecto)
    tipo_producto = CharField(max_length=50, null=True)
    id_categoria = IntegerField()  
    id_proveedor = IntegerField()  

    class Meta:
        table_name = 'producto'