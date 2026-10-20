from datos.modelos.producto_almacen import ProductoAlmacen
from auxiliares.datos_inventario import mensaje_error

def listado_productos_almacenes():
    try:
        productos_almacenes = ProductoAlmacen.select()
        if productos_almacenes:
            return list(productos_almacenes)
    except Exception as error:
        print(f'{mensaje_error}: {error}')
        return []

def guardar_producto_almacen(producto_almacen: ProductoAlmacen):
    try:
        respuesta = producto_almacen.save()
        if respuesta == 1:
            print(f'Se ha guardado con éxito el registro ID: {producto_almacen.id_registro}')
            return producto_almacen
    except Exception as error:
        print(f'{mensaje_error}: {error}')
        return None