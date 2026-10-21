from datos.modelos.movimiento_inventario import MovimientoInventario
from auxiliares.datos_inventario import mensaje_error

def listado_movimientos():
    try:
        movimientos = MovimientoInventario.select()
        if movimientos:
            return movimientos
    except Exception as error:
        print(f'{mensaje_error}: {error}')

def obtener_movimiento_nombre(nombre_movimiento):
    try:
        movimiento = MovimientoInventario.get(MovimientoInventario.nombre_movimiento == nombre_movimiento)
        if movimiento:
            return movimiento
    except Exception as error:
        print(f'{mensaje_error}: {error}')

def guardar_movimiento(movimiento: MovimientoInventario):
    try:
        respuesta = movimiento.save()
        if respuesta == 1:
            print(f'Se ha registrado con éxito: {movimiento.movimiento}')
    except Exception as error:
        print(f'{mensaje_error}: {error}')

