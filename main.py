import sys
from presentacion.presentacion_usuario import login_usuario, crear_usuario
from presentacion.menu import cargar_menu

def menu_acceso():
    while True:
        print('====================================')
        print('   BIENVENIDO A INVENTARIO PYME')
        print('====================================')
        print('[1] - Iniciar Sesión')
        print('[2] - Crear Cuenta (Registrarse)')
        print('[0] - Salir\n')

        opcion = input('Seleccione una opción: ').strip()

        match opcion:
            case '1':
                usuario_autenticado = login_usuario()
                if usuario_autenticado:
                    cargar_menu(usuario_autenticado)
            case '2':
                crear_usuario(es_registro_publico=True)
            case '0':
                print('\nSaliendo del sistema...')
                sys.exit()
            case _:
                print('\nOpción no válida. Intente nuevamente.\n')

if __name__ == '__main__':
    menu_acceso()