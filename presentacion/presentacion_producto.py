from prettytable import PrettyTable
from auxiliares.datos_inventario import mensaje_error
from negocio import procesar_listado_productos

def mostrar_listado_productos():
    try:
        tabla_productos = PrettyTable()
        tabla_resultado = procesar_listado_productos(tabla_productos)
        if tabla_resultado:
            print('\n--- LISTADO DE PRODUCTOS ---')
            print(tabla_resultado)
            print()
        else:
            print('\nNo hay productos registrados en el sistema.\n')
    except Exception as error:
        print(f'{mensaje_error}: {error}')