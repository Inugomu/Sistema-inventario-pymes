from datos.modelos.almacen import Almacen
from auxiliares.datos_inventario import mensaje_error

def listado_almacenes():
    try:
        almacenes = Almacen.select().where(Almacen.habilitado == 1)
        if almacenes:
            return list(almacenes)
    except Exception as error:
        print(f'{mensaje_error}: {error}')
        return []

def obtener_almacen_id(id_almacen):
    try:
        return Almacen.get_or_none((Almacen.id_almacen == id_almacen) & (Almacen.habilitado == 1))
    except Exception as error:
        print(f'{mensaje_error}: {error}')
        return None

def obtener_almacen_nombre(nombre_almacen):
    try:
        return Almacen.get_or_none(Almacen.nombre_almacen == nombre_almacen)
    except Exception as error:
        print(f'{mensaje_error}: {error}')
        return None

def guardar_almacen(almacen: Almacen):
    try:
        respuesta = almacen.save()
        if respuesta == 1:
            print(f'Se ha guardado con éxito el almacén: {almacen.nombre_almacen}')
            return almacen
    except Exception as error:
        print(f'{mensaje_error}: {error}')
        return None