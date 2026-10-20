import sys
from presentacion import (
    mostrar_listado_almacenes, 
    mostrar_listado_productos, 
    mostrar_listado_movimientos
)

def cargar_menu():
    while True:
        print('====================================')
        print('   SISTEMA DE INVENTARIO PYME')
        print('====================================')
        print('[1] - Listar Almacenes')
        print('[2] - Listar Productos')
        print('[3] - Listar Movimientos de Inventario')
        print('[0] - Salir\n')

        opcion = input('Seleccione una opción: ').strip()

        match opcion:
            case '1':
                mostrar_listado_almacenes()
            case '2':
                mostrar_listado_productos()
            case '3':
                mostrar_listado_movimientos()
            case '0':
                print('\nSaliendo del sistema...')
                sys.exit()
            case _:
                print('\nOpción no válida. Intente nuevamente.\n')