from datos.modelos.producto_perecible import ProductoPerecible
from auxiliares.datos_inventario import mensaje_error

def listado_productos_perecibles():
    try:
        productos_perecibles = ProductoPerecible.select()
        if productos_perecibles:
            return productos_perecibles
    except Exception as error:
        print(f'{mensaje_error}: {error}')

def obtener_producto_perecible(nombre_producto_perecible):
    try:
        producto_perecible = ProductoPerecible.get(ProductoPerecible.producto_perecible == nombre_producto_perecible)
        if producto_perecible:
            return producto_perecible
    except Exception as error:
        print(f'{mensaje_error}: {error}')

def guardar_producto_perecible(producto: ProductoPerecible):
    try:
        respuesta = producto.save()
        if respuesta == 1:
            print(f'Se ha guardado con éxito: {producto.producto_perecible}')
    except Exception as error:
        print(f'{mensaje_error}: {error}')
