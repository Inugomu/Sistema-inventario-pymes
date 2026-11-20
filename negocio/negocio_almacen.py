from prettytable import PrettyTable
from datos.modelos.almacen import Almacen
from datos.repositorios.repo_almacen import listado_almacenes, obtener_almacen_id, guardar_almacen
from auxiliares.datos_inventario import mensaje_error

def procesar_listado_almacenes(tabla: PrettyTable):
    if tabla is not None:
        tabla.field_names = ['ID', 'Nombre Almacén', 'Dirección', 'Capacidad Máxima']
        almacenes = listado_almacenes()
        if almacenes:
            for almacen in almacenes:
                tabla.add_row([
                    almacen.id_almacen,
                    almacen.nombre_almacen,
                    almacen.direccion if almacen.direccion else 'N/A',
                    almacen.capacidad_maxima
                ])
            return tabla
    return None

def almacen_por_id(id_almacen: int):
    return obtener_almacen_id(id_almacen)

def crear_objeto_almacen(nombre: str, direccion: str, capacidad: int):
    try:
        almacen = Almacen()
        almacen.nombre_almacen = nombre
        almacen.direccion = direccion if direccion else None
        almacen.capacidad_maxima = capacidad
        almacen.habilitado = 1
        return guardar_almacen(almacen)
    except Exception as error:
        print(f'{mensaje_error}: {error}')
        return None

def modificar_objeto_almacen(nombre: str, direccion: str, capacidad: int, almacen: Almacen):
    try:
        if nombre:
            almacen.nombre_almacen = nombre
        if direccion:
            almacen.direccion = direccion
        if capacidad is not None:
            almacen.capacidad_maxima = capacidad
        return guardar_almacen(almacen)
    except Exception as error:
        print(f'{mensaje_error}: {error}')
        return None

def deshabilitar_objeto_almacen(almacen: Almacen):
    try:
        almacen.habilitado = 0
        return guardar_almacen(almacen)
    except Exception as error:
        print(f'{mensaje_error}: {error}')
        return None