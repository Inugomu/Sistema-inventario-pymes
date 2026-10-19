from datos.modelos.movimiento_inventario import Movimiento_inventario
from auxiliares import mensaje_error

def listado_moviemientos():
    try:
        moviemientos = Movimiento.select()
        if movimientos:
            return moviemientos
    except Exception as error:
        print(f'{mensaje_error}{error}')

def obtener_movimiento_nombre(nombre_movimiento):
    try:
        movimiento = Movimiento_inventario.get(Movimiento_inventario.movimiento == nombre_movimiento)
        if movimiento:
            return movimiento
    except Exception as error:
        print(f'{mensaje_error}{error}')

def guardar_movimiento(movimiento):
    try:
        respuesta = movimiento()
        if respuesta == 1:
            return movimiento
            print(f'Se ha guardado con éxito: {movimiento.Movimiento}')
    except Exception as error:
        print(f'{mensaje_error}{error}')
