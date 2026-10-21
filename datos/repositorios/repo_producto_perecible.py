from datos.modelos.producto_perecible import ProductoPerecible
from auxiliares.datos_inventario import mensaje_error

def listado_productos_perecibles():
    try:
        productos_perecibles = ProductoPerecible.select()
        if productos_perecibles:
            return list(productos_perecibles)
    except Exception as error:
        print(f'{mensaje_error}: {error}')
        return []

def obtener_producto_perecible(nombre_producto_perecible):
    try:
        producto_perecible = ProductoPerecible.get(ProductoPerecible.producto_perecible == nombre_producto_perecible)
        if producto_perecible:
            return producto_perecible
    except Exception as error:
        print(f'{mensaje_error}: {error}')
        return None

def guardar_producto_perecible(producto: ProductoPerecible):
    try:
        respuesta = producto.save(force_insert=True)
        if respuesta == 1:
            print(f'Se ha guardado con éxito: {producto.producto_perecible}')
            return producto
    except Exception as error:
        print(f'{mensaje_error}: {error}')
        return None
    
