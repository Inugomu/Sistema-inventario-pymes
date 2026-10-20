from prettytable import PrettyTable
from datos.repositorios.repo_almacen import listado_almacenes

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