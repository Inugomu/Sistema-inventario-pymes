from datos.modelos.almacen import Almacen
from auxiliares.datos_inventario import mensaje_error

def listado_almacenes():
    try:
        almacenes = Almacen.select()
        if almacenes:
            return list(almacenes)
    except Exception as error:
        print(f'{mensaje_error}: {error}')
        return []

def obtener_almacen_nombre(nombre_almacen):
    try:
        almacen = Almacen.get(Almacen.nombre_almacen == nombre_almacen)
        if almacen:
            return almacen
    except Exception as error:
        print(f'{mensaje_error}: {error}')
        return None

def guardar_almacen(almacen: Almacen):
    try:
        respuesta = almacen.save()
        if respuesta == 1:
            print(f'Se ha guardado con éxito: {almacen.nombre_almacen}')
            return almacen
    except Exception as error:
        print(f'{mensaje_error}: {error}')
        return None