from peewee import AutoField, IntegerField, Model
from datos.conexion import conectar

base_datos = conectar()

class BaseModel(Model):
    class Meta:
        database = base_datos

class EntradaInventario(BaseModel):
    id_entrada = AutoField()  
    id_movimiento = IntegerField()  
    id_proveedor = IntegerField()  

    class Meta:
        table_name = 'entrada_inventario'