from datos.modelos.producto_perecible import ProductoPerecible
from auxiliares.datos_inventario import mensaje_error

def listado_productos_perecibles():
    try:
        productos = ProductoPerecible.select()
        if productos:
            return list(productos)
    except Exception as error:
        print(f'{mensaje_error}: {error}')
        return []

def obtener_producto_perecible_por_id(id_producto):
    try:
        return ProductoPerecible.get(ProductoPerecible.id_producto == id_producto)
    except Exception as error:
        print(f'{mensaje_error}: {error}')
        return None

def guardar_producto_perecible(producto: ProductoPerecible):
    try:
        respuesta = producto.save(force_insert=True)
        if respuesta == 1:
            print(f'Se ha guardado producto perecible ID: {producto.id_producto}')
            return producto
    except Exception as error:
        print(f'{mensaje_error}: {error}')
        return None