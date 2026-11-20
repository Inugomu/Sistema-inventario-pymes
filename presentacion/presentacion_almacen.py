from prettytable import PrettyTable
from auxiliares.datos_inventario import mensaje_error
from negocio import procesar_listado_almacenes

def mostrar_listado_almacenes():
    try:
        tabla_almacenes = PrettyTable()
        tabla_resultado = procesar_listado_almacenes(tabla_almacenes)
        if tabla_resultado:
            print('\n--- LISTADO DE ALMACENES ---')
            print(tabla_resultado)
            print()
        else:
            print('\nNo hay almacenes para mostrar o no se pudo cargar la información.\n')
    except Exception as error:
        print(f'{mensaje_error}: {error}')