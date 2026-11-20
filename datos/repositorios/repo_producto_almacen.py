from datos.modelos.producto_almacen import ProductoAlmacen
from auxiliares.datos_inventario import mensaje_error

def listado_productos_almacenes():
    try:
        productos_almacenes = ProductoAlmacen.select()
        if productos_almacenes:
            return productos_almacenes
    except Exception as error:
        print(f'{mensaje_error}: {error}')

def obtener_producto_almacen(nombre_producto_almacen):
    try:
        producto_almacen = ProductoAlmacen.get(ProductoAlmacen.producto_almacen == nombre_producto_almacen)
        if producto_almacen:
            return producto_almacen
    except Exception as error:
        print(f'{mensaje_error}: {error}')

def guardar_producto_almacen(producto_almacen: ProductoAlmacen):
    try:
        respuesta = producto_almacen.save()
        if respuesta == 1:
            print(f'Se ha guardado con éxito: {producto_almacen.producto_almacen}')
    except Exception as error:
        print(f'{mensaje_error}: {error}')
