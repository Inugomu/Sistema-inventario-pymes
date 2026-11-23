from datos.modelos.producto import Producto
from auxiliares.datos_inventario import mensaje_error

def listado_productos():
    try:
        productos = Producto.select().where(Producto.habilitado == 1)
        if productos:
            return list(productos)
    except Exception as error:
        print(f'{mensaje_error}: {error}')
        return []

def obtener_producto_id(id_producto):
    try:
        return Producto.get_or_none((Producto.id_producto == id_producto) & (Producto.habilitado == 1))
    except Exception as error:
        print(f'{mensaje_error}: {error}')
        return None

def obtener_producto_nombre(nombre_producto):
    try:
        return Producto.get_or_none(Producto.nombre == nombre_producto)
    except Exception as error:
        print(f'{mensaje_error}: {error}')
        return None

def guardar_producto(producto: Producto):
    try:
        respuesta = producto.save()
        if respuesta == 1:
            print(f'Se ha guardado con éxito el producto: {producto.nombre}')
            return producto
    except Exception as error:
        print(f'{mensaje_error}: {error}')
        return None