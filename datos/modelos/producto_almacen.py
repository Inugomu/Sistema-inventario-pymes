from peewee import AutoField, IntegerField, Model
from datos.conexion import conectar
from auxiliares.datos_inventario import defecto

base_datos = conectar()

class BaseModel(Model):
    class Meta:
        database = base_datos

class ProductoAlmacen(BaseModel):
    id_registro = AutoField()
    id_producto = IntegerField()  
    id_almacen = IntegerField()   
    cantidad = IntegerField(defecto)

    class Meta:
        table_name = 'producto_almacen'