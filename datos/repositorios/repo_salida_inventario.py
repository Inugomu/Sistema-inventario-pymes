from datos.modelos.salida_inventario import SalidaInventario
from auxiliares import mensaje_error

def listado_salidas():
    try:
        salida_inventario = SalidaInventario.select()
        if salidas
            return salidas
    except Exception as error:
        print(f'{mensaje_error}{error}')

def obtener_salida_nombre(nombre_salida):
    try:
        salida_inventario = SalidaInventario.get(SalidaInventario.salida_inventario == nombre_salida)
        if salida
            return salida
    except Exception as error:
        print(f'{mensaje_error}{error}')

def guardar_salida(salida_inventario:SalidaInventario):
    try:
        respuesta = salida_inventario.save()
        if respuesta == 1:
            return salida_inventario
            print(f'Se ha guardado con éxito: {almacen.almacen}')
    except Exception as error:
        print(f'{mensaje_error}{error}')

