from presentacion.presentacion_almacen import (
    mostrar_listado_almacenes,
    registrar_nuevo_almacen,
    modificar_almacen,
    eliminar_almacen
)
from presentacion.presentacion_producto import (
    mostrar_listado_productos,
    registrar_nuevo_producto,
    modificar_producto,
    eliminar_producto
)
from presentacion.presentacion_movimiento import (
    mostrar_listado_movimientos,
    registrar_movimiento_inventario
)
from presentacion.presentacion_usuario import (
    mostrar_listado_usuarios,
    crear_usuario,
    modificar_usuario,
    eliminar_usuario
)

def cargar_menu_almacenes():
    while True:
        print('------------------------------------')
        print('       GESTIÓN DE ALMACENES')
        print('------------------------------------')
        print('[1] - Listar Almacenes')
        print('[2] - Registrar Nuevo Almacén')
        print('[3] - Modificar Almacén')
        print('[4] - Eliminar Almacén')
        print('[0] - Volver al Menú Principal\n')

        opcion = input('Seleccione una opción: ').strip()
        match opcion:
            case '1':
                mostrar_listado_almacenes()
            case '2':
                registrar_nuevo_almacen()
            case '3':
                modificar_almacen()
            case '4':
                eliminar_almacen()
            case '0':
                print()
                break
            case _:
                print('\nOpción no válida. Intente nuevamente.\n')

def cargar_menu_productos():
    while True:
        print('------------------------------------')
        print('       GESTIÓN DE PRODUCTOS')
        print('------------------------------------')
        print('[1] - Listar Productos y Stock')
        print('[2] - Ingresar Nuevo Producto')
        print('[3] - Modificar Producto')
        print('[4] - Eliminar Producto')
        print('[0] - Volver al Menú Principal\n')

        opcion = input('Seleccione una opción: ').strip()
        match opcion:
            case '1':
                mostrar_listado_productos()
            case '2':
                registrar_nuevo_producto()
            case '3':
                modificar_producto()
            case '4':
                eliminar_producto()
            case '0':
                print()
                break
            case _:
                print('\nOpción no válida. Intente nuevamente.\n')

def cargar_menu_movimientos():
    while True:
        print('------------------------------------')
        print('   MOVIMIENTOS Y CONTROL DE STOCK')
        print('------------------------------------')
        print('[1] - Historial de Movimientos')
        print('[2] - Registrar Entrada / Salida de Stock')
        print('[0] - Volver al Menú Principal\n')

        opcion = input('Seleccione una opción: ').strip()
        match opcion:
            case '1':
                mostrar_listado_movimientos()
            case '2':
                registrar_movimiento_inventario()
            case '0':
                print()
                break
            case _:
                print('\nOpción no válida. Intente nuevamente.\n')

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
    es_admin = usuario_actual and usuario_actual.rol == 'ADMINISTRADOR'
    nombre_sesion = f'{usuario_actual.nombre} ({usuario_actual.rol})' if usuario_actual else 'Invitado'

    while True:
        print('====================================')
        print('   SISTEMA DE INVENTARIO PYME')
        print(f'   Sesión: {nombre_sesion}')
        print('====================================')
        print('[1] - Gestión de Almacenes')
        print('[2] - Gestión de Productos')
        print('[3] - Movimientos y Control de Stock')
        if es_admin:
            print('[4] - Gestión de Usuarios (Admin)')
        print('[0] - Cerrar Sesión\n')

        opcion = input('Seleccione una opción: ').strip()

        match opcion:
            case '1':
                cargar_menu_almacenes()
            case '2':
                cargar_menu_productos()
            case '3':
                cargar_menu_movimientos()
            case '4' if es_admin:
                cargar_menu_usuarios()
            case '0':
                print('\nCerrando sesión...\n')
                break
            case _:
                print('\nOpción no válida o sin permisos suficientes.\n')