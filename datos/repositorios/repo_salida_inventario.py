from datos.modelos.salida_inventario import SalidaInventario
from auxiliares import mensaje_error

def listado_salidas():
    try:
        salidas = SalidaInventario.select()
        if salidas:
            return salidas
    except Exception as error:
        print(f'{mensaje_error}{error}')

def obtener_salida_nombre(nombre_salida):
    try:
        salida = SalidaInventario.get(SalidaInventario.salida_inventario == nombre_salida)
        if salida:
            return salida
    except Exception as error:
        print(f'{mensaje_error}{error}')

def guardar_salida(salida_inventario:SalidaInventario):
    try:
        respuesta = salida_inventario.save()
        if respuesta == 1:
            return salida_inventario
            print(f'Se ha guardado con éxito: {salida_inventario}')
    except Exception as error:
        print(f'{mensaje_error}{error}')

