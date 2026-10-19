from datos.modelos.almacen import Almacen
from auxiliares import mensaje_error

def listado_almacenes():
    try:
        almacenes = Almacen.select()
        if almacenes:
            return almacenes
    except Exception as error:
        print(f'{mensaje_error}{error}')

def obtener_almacen_nombre(nombre_almacen):
    try:
        almacen = Almacen.get(Almacen.almacen == nombre_almacen)
        if almacen:
            return almacen
    except Exception as error:
        print(f'{mensaje_error}{error}')

def guardar_almacen(almacen:Almacen):
    try:
        respuesta = almacen.save()
        if respuesta == 1:
            return almacen
            print(f'Se ha guardado con éxito: {almacen.almacen}')
    except Exception as error:
        print(f'{mensaje_error}{error}')


