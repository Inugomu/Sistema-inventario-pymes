from datos.modelos.movimiento_inventario import MovimientoInventario
from auxiliares.datos_inventario import mensaje_error

def listado_movimientos():
    try:
        movimientos = MovimientoInventario.select().order_by(MovimientoInventario.id_movimiento.desc())
        if movimientos:
            return list(movimientos)
    except Exception as error:
        print(f'{mensaje_error}: {error}')
        return []

def guardar_movimiento(movimiento: MovimientoInventario):
    try:
        respuesta = movimiento.save()
        if respuesta == 1:
            print(f'Movimiento ({movimiento.tipo_movimiento}) registrado con éxito.')
            return movimiento
    except Exception as error:
        print(f'{mensaje_error}: {error}')
        return None
