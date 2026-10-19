from datos.modelos.producto_perecible import Producto_perecible
from auxiliares import mensaje_error

def listado_productos_perecibles():
    try:
        productos = Producto_perecible.select()
        if productos:
            return productos
    except Exception as error:
        print(f'{mensaje_error}{error}')

def obtener_producto_perecible_nombre(nombre_producto):
    try:
        producto = Producto_perecible.get(Producto_perecible.producto == nombre_producto)
        if producto:
            return producto
    except Exception as error:
        print(f'{mensaje_error}{error}')

def guardar_producto_perecible(producto:Producto_perecible):
    try:
        respuesta = producto.save()
        if respuesta == 1:
            print (f'Se ha guardado con éxito: {producto.producto}')
    except Exception as error:
        print(f'{mensaje_error}{error}')


        