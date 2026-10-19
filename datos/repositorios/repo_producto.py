from datos.modelos.producto import producto
from auxiliares import mensaje_error

def listado_productos():
    try:
        productos = Producto.select()
        if productos:
            return productos
    except Exception as error:
        print(f'{mensaje_error}{error}')

def obtener_producto_nombre(nombre_producto):
    try:
        producto = Producto.get(Producto.producto == nombre_almacen)
        if producto:
            return producto
    except Exception as error:
        print(f'{mensaje_error}{error}')

def guardar_producto(producto:Producto):
    try:
        respuesta = producto.save()
        if respuesta == 1:
            print (f'Se ha guardado con éxito: {producto.producto}')
    except Exception as error:
        print(f'{mensaje_error}{error}')



