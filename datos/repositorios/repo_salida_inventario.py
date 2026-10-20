from datos.modelos.salida_inventario import SalidaInventario
from auxiliares.datos_inventario import mensaje_error

def listado_salidas():
    try:
        salidas = SalidaInventario.select()
        if salidas:
            return list(salidas)
    except Exception as error:
        print(f'{mensaje_error}: {error}')
        return []

def obtener_salida_por_id(id_movimiento):
    try:
        return SalidaInventario.get(SalidaInventario.id_movimiento == id_movimiento)
    except Exception as error:
        print(f'{mensaje_error}: {error}')
        return None

def guardar_salida(salida: SalidaInventario):
    try:
        respuesta = salida.save(force_insert=True)
        if respuesta == 1:
            print(f'Se ha guardado la salida para el movimiento ID: {salida.id_movimiento}')
            return salida
    except Exception as error:
        print(f'{mensaje_error}: {error}')
        return None