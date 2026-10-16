from peewee import AutoField, IntegerField, Model
from datos.conexion import conectar

base_datos = conectar()

class BaseModel(Model):
    class Meta:
        database = base_datos

class EntradaInventario(BaseModel):
    id_entrada = AutoField()  # O id_movimiento si actúa como clave primaria/foránea
    id_movimiento = IntegerField()  # O ForeignKeyField(MovimientoInventario, ...)
    id_proveedor = IntegerField()   # O ForeignKeyField(Proveedor, ...)

    class Meta:
        table_name = 'entrada_inventario'