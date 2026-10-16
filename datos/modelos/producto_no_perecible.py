from peewee import AutoField, IntegerField, Model
from datos.conexion import conectar

base_datos = conectar()

class BaseModel(Model):
    class Meta:
        database = base_datos

class ProductoNoPerecible(BaseModel):
    id_no_perecible = AutoField()
    id_producto = IntegerField()  
    garantia_meses = IntegerField()

    class Meta:
        table_name = 'producto_no_perecible'