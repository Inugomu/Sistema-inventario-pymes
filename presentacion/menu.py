import sys
from presentacion import mostrar_listado_almacenes

def cargar_menu():
    while True:
        print('====================================')
        print('   SISTEMA DE INVENTARIO PYME')
        print('====================================')
        print('[1] - Listar Almacenes')
        print('[2] - Gestionar Productos (En desarrollo)')
        print('[3] - Gestionar Movimientos (En desarrollo)')
        print('[0] - Salir\n')

        opcion = input('Seleccione una opción: ').strip()

        match opcion:
            case '1':
                mostrar_listado_almacenes()
            case '2':
                print('\nMódulo de productos en desarrollo...\n')
            case '3':
                print('\nMódulo de movimientos en desarrollo...\n')
            case '0':
                print('\nSaliendo del sistema...')
                sys.exit()
            case _:
                print('\nOpción no válida. Intente nuevamente.\n')