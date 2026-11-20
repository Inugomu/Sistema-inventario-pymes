import sys
from presentacion.presentacion_almacen import mostrar_listado_almacenes
from presentacion.presentacion_producto import mostrar_listado_productos
from presentacion.presentacion_movimiento import mostrar_listado_movimientos
from presentacion.presentacion_usuario import (
    mostrar_listado_usuarios,
    crear_usuario,
    modificar_usuario,
    eliminar_usuario
)

def cargar_menu_usuarios():
    while True:
        print('------------------------------------')
        print('        GESTIÓN DE USUARIOS')
        print('------------------------------------')
        print('[1] - Listar Usuarios')
        print('[2] - Registrar Usuario')
        print('[3] - Modificar Usuario')
        print('[4] - Eliminar Usuario')
        print('[0] - Volver al Menú Principal\n')

        opcion = input('Seleccione una opción: ').strip()

        match opcion:
            case '1':
                mostrar_listado_usuarios()
            case '2':
                crear_usuario()
            case '3':
                modificar_usuario()
            case '4':
                eliminar_usuario()
            case '0':
                print()
                break
            case _:
                print('\nOpción no válida. Intente nuevamente.\n')

def cargar_menu(usuario_actual=None):
    while True:
        print('====================================')
        print('   SISTEMA DE INVENTARIO PYME')
        print('====================================')
        print('[1] - Listar Almacenes')
        print('[2] - Listar Productos')
        print('[3] - Listar Movimientos de Inventario')
        print('[4] - Gestión de Usuarios')
        print('[0] - Cerrar Sesión y Salir\n')

        opcion = input('Seleccione una opción: ').strip()

        match opcion:
            case '1':
                mostrar_listado_almacenes()
            case '2':
                mostrar_listado_productos()
            case '3':
                mostrar_listado_movimientos()
            case '4':
                cargar_menu_usuarios()
            case '0':
                print('\nCerrando sesión y saliendo del sistema...')
                sys.exit()
            case _:
                print('\nOpción no válida. Intente nuevamente.\n')