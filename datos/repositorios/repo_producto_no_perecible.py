from datos.modelos.producto_no_perecible import ProductoNoPerecible
from auxiliares.datos_inventario import mensaje_error

def listado_productos_no_perecibles():
    try:
        productos_no_perecibles = ProductoNoPerecible.select()
        if productos_no_perecibles:
            return productos_no_perecibles
    except Exception as error:
        print(f'{mensaje_error}: {error}')

def obtener_producto_no_perecible_por_nombre(nombre_producto):
    try:
        producto_no_perecible = ProductoNoPerecible.get(ProductoNoPerecible.nombre_producto == nombre_producto)
        if producto_no_perecible:
            return producto_no_perecible
    except Exception as error:
        print(f'{mensaje_error}: {error}')

def guardar_producto_no_perecible(producto: ProductoNoPerecible):
    try:
        respuesta = producto.save()
        if respuesta == 1:
            print(f'Se ha guardado con éxito: {producto.producto_no_perecible}')
    except Exception as error:
        print(f'{mensaje_error}: {error}')

