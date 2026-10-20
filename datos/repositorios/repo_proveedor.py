from datos.modelos.proveedor import Proveedor
from auxiliares.datos_inventario import mensaje_error

def listado_proveedores():
    try:
        proveedores = Proveedor.select()
        if proveedores:
            return list(proveedores)
    except Exception as error:
        print(f'{mensaje_error}: {error}')
        return []

def obtener_proveedor_nombre(nombre_proveedor):
    try:
        return Proveedor.get(Proveedor.nombre == nombre_proveedor)
    except Exception as error:
        print(f'{mensaje_error}: {error}')
        return None

def guardar_proveedor(proveedor: Proveedor):
    try:
        respuesta = proveedor.save()
        if respuesta == 1:
            print(f'Se ha guardado con éxito: {proveedor.nombre}')
            return proveedor
    except Exception as error:
        print(f'{mensaje_error}: {error}')
        return None