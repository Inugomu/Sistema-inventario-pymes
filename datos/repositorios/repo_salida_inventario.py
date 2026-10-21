from datos.modelos.salida_inventario import SalidaInventario
from auxiliares.datos_inventario import mensaje_error

def listado_salidas():
    try:
        salidas = SalidaInventario.select()
        if salidas:
            return salidas
    except Exception as error:
        print(f'{mensaje_error}: {error}')

def obtener_salida_por_nombre(nombre_salida):
    try:
        salida = SalidaInventario.get(SalidaInventario.nombre == nombre_salida)
        if salida:
            return salida
    except Exception as error:
        print(f'{mensaje_error}: {error}')

def guardar_salida(salida: SalidaInventario):
    try:
        respuesta = salida.save()
        if respuesta == 1:
            print(f'Se ha guardado con exito: {salida.salida}')
    except Exception as error:
        print(f'{mensaje_error}: {error}')

