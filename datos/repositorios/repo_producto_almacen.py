from datos.modelos.producto_almacen import Producto_almacen
from auxiliares import mensaje_error

def listado_productos_almacenes():
    try:
        productos_almacenes = Producto_almacen.select()
        if productos_almacenes:
            return productos_almacenes
    except Exception as error:
        print(f'{mensaje_error}{error}')

def obtener_producto_almacen_nombre(nombre_producto_almacen):
    try:
        producto_almacen = Producto_almacen.get(Producto_almacen.producto_almacen == nombre_producto_almacen)
        if producto_almacen:
            return producto_almacen
    except Exception as error:
        print(f'{mensaje_error}{error}')

def guardar_producto_almacen(producto_almacen:Producto_almacen):
    try:
        respuesta = producto_almacen.save()
        if respuesta == 1:
            return producto_almacen
            print(f'Se ha guardado con éxito: {almacen.almacen}')
    except Exception as error:
        print(f'{mensaje_error}{error}')

