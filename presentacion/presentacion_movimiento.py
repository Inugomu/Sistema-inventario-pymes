from prettytable import PrettyTable
from auxiliares.datos_inventario import mensaje_error
from negocio.negocio_movimiento import procesar_listado_movimientos

def mostrar_listado_movimientos():
    try:
        tabla_movimientos = PrettyTable()
        tabla_resultado = procesar_listado_movimientos(tabla_movimientos)
        if tabla_resultado:
            print('\n--- LISTADO DE MOVIMIENTOS DE INVENTARIO ---')
            print(tabla_resultado)
            print()
        else:
            print('\nNo hay movimientos registrados en la base de datos.\n')
    except Exception as error:
        print(f'{mensaje_error}: {error}')