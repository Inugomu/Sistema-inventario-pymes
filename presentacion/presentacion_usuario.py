import maskpass
from prettytable import PrettyTable
from auxiliares.datos_inventario import mensaje_error
from auxiliares.validaciones import (
    validar_rut,
    validar_largo_string,
    validar_correo,
    validar_contrasena
)
from negocio.negocio_usuario import (
    procesar_listado_usuarios,
    crear_objeto_usuario,
    modificar_objeto_usuario,
    deshabilitar_objeto_usuario,
    usuario_por_rut,
    usuario_por_correo,
    autenticar_usuario
)

def solicitar_rut(prompt, opcional=False, permitir_volver=False):
    while True:
        rut = input(prompt).strip()
        if permitir_volver and rut == '0':
            return None
        if opcional and rut == '':
            return ''
        rut_valido, mensaje = validar_rut(rut)
        print(mensaje)
        if rut_valido != '':
            return rut_valido

def solicitar_texto(prompt, largo=50, opcional=False, permitir_volver=False):
    while True:
        valor = input(prompt).strip()
        if permitir_volver and valor == '0':
            return None
        if opcional and valor == '':
            return ''
        valor_valido, mensaje = validar_largo_string(valor, largo)
        print(mensaje)
        if valor_valido != '':
            return valor_valido

def solicitar_correo(prompt, opcional=False, permitir_volver=False):
    while True:
        correo = input(prompt).strip()
        if permitir_volver and correo == '0':
            return None
        if opcional and correo == '':
            return ''
        correo_valido, mensaje = validar_correo(correo)
        print(mensaje)
        if correo_valido != '':
            return correo_valido

def solicitar_rol(opcional=False, permitir_volver=False):
    while True:
        print('Roles disponibles: [1] ADMINISTRADOR  [2] OPERADOR' + ('  [0] Volver' if permitir_volver else ''))
        opcion = input('Seleccione rol (ENTER para conservar/por defecto): ').strip()
        if permitir_volver and opcion == '0':
            return None
        if opcional and opcion == '':
            return ''
        if opcion == '1':
            return 'ADMINISTRADOR'
        if opcion == '2' or opcion == '':
            return 'OPERADOR'
        print('Opción inválida.\n')

def solicitar_contrasena_segura(prompt, permitir_volver=False):
    while True:
        print('\nRequisitos de contraseña:')
        print('- Entre 8 y 15 caracteres')
        print('- Al menos 1 mayúscula, 1 minúscula y 1 número')
        print('- Al menos 1 símbolo: !@#$%&/')
        if permitir_volver:
            print('- Ingrese 0 para cancelar y volver')
        contrasena = maskpass.askpass(prompt=prompt, mask='*')
        if permitir_volver and contrasena == '0':
            return None
        valida, errores = validar_contrasena(contrasena)
        if errores:
            print('\nContraseña inválida:')
            for err in errores:
                print(f'  - {err}')
        else:
            return valida

def mostrar_listado_usuarios():
    try:
        tabla = PrettyTable()
        resultado = procesar_listado_usuarios(tabla)
        if resultado:
            print('\n--- LISTADO DE USUARIOS ---')
            print(resultado)
            print()
        else:
            print('\nNo hay usuarios habilitados para mostrar.\n')
    except Exception as error:
        print(f'{mensaje_error}: {error}')

def crear_usuario(es_registro_publico=False):
    print('\n=== REGISTRAR NUEVO USUARIO ===')
    print('(Ingrese 0 en cualquier campo para volver al menú)\n')

    rut = solicitar_rut('RUT (ej. 12345678-9): ', permitir_volver=True)
    if rut is None:
        print('\nRegistro cancelado. Volviendo al menú...\n')
        return
    if usuario_por_rut(rut):
        print('Error: Ya existe un usuario registrado con ese RUT.\n')
        return

    nombre = solicitar_texto('Nombre: ', largo=50, permitir_volver=True)
    if nombre is None:
        print('\nRegistro cancelado. Volviendo al menú...\n')
        return

    apellido = solicitar_texto('Apellido: ', largo=50, permitir_volver=True)
    if apellido is None:
        print('\nRegistro cancelado. Volviendo al menú...\n')
        return

    correo = solicitar_correo('Correo electrónico: ', permitir_volver=True)
    if correo is None:
        print('\nRegistro cancelado. Volviendo al menú...\n')
        return
    if usuario_por_correo(correo):
        print('Error: Ya existe una cuenta registrada con ese correo.\n')
        return
    
    if es_registro_publico:
        rol = 'OPERADOR'
    else:
        rol = solicitar_rol(permitir_volver=True)
        if rol is None:
            print('\nRegistro cancelado. Volviendo al menú...\n')
            return
        
    contrasena = solicitar_contrasena_segura('Contraseña: ', permitir_volver=True)
    if contrasena is None:
        print('\nRegistro cancelado. Volviendo al menú...\n')
        return

    crear_objeto_usuario(rut, nombre, apellido, correo, contrasena, rol)
    print()

def modificar_usuario():
    print('\n=== MODIFICAR USUARIO ===')
    rut_buscar = solicitar_rut('Ingrese RUT del usuario a modificar (0 para volver): ', permitir_volver=True)
    if rut_buscar is None:
        print('\nOperación cancelada.\n')
        return

    usuario = usuario_por_rut(rut_buscar)
    if not usuario:
        print('Usuario no encontrado.\n')
        return

    print(f'Editando a: {usuario.nombre} {usuario.apellido} ({usuario.correo})\n')
    nuevo_rut = solicitar_rut('Nuevo RUT (ENTER para conservar): ', opcional=True)
    if nuevo_rut and nuevo_rut != usuario.rut and usuario_por_rut(nuevo_rut):
        print('Error: Ese RUT ya pertenece a otro usuario.\n')
        return

    nuevo_nombre = solicitar_texto('Nuevo Nombre (ENTER para conservar): ', largo=50, opcional=True)
    nuevo_apellido = solicitar_texto('Nuevo Apellido (ENTER para conservar): ', largo=50, opcional=True)
    nuevo_correo = solicitar_correo('Nuevo Correo (ENTER para conservar): ', opcional=True)
    if nuevo_correo and nuevo_correo.lower() != usuario.correo and usuario_por_correo(nuevo_correo):
        print('Error: Ese correo ya pertenece a otro usuario.\n')
        return

    nuevo_rol = solicitar_rol(opcional=True)

    modificar_objeto_usuario(nuevo_rut, nuevo_nombre, nuevo_apellido, nuevo_correo, nuevo_rol, usuario)
    print()

def eliminar_usuario():
    print('\n=== ELIMINAR (DESHABILITAR) USUARIO ===')
    rut_buscar = solicitar_rut('Ingrese RUT del usuario a eliminar (0 para volver): ', permitir_volver=True)
    if rut_buscar is None:
        print('\nOperación cancelada.\n')
        return

    usuario = usuario_por_rut(rut_buscar)
    if not usuario:
        print('Usuario no encontrado.\n')
        return

    confirmacion = input(f'¿Está seguro de deshabilitar a {usuario.nombre} {usuario.apellido}? [S/N]: ').strip().lower()
    if confirmacion == 's':
        deshabilitar_objeto_usuario(usuario)
    else:
        print('Operación cancelada.')
    print()

def login_usuario():
    intentos_maximos = 3
    intentos = 0

    print('\n====================================')
    print('  INICIO DE SESIÓN - INVENTARIO PYME')
    print('  (Ingrese 0 para volver al menú)')
    print('====================================')

    while intentos < intentos_maximos:
        correo = solicitar_correo('Correo: ', permitir_volver=True)
        if correo is None:
            print('\nVolviendo al menú principal...\n')
            return None

        usuario_registrado = usuario_por_correo(correo)
        if not usuario_registrado or not usuario_registrado.habilitado:
            print('El usuario no existe o se encuentra deshabilitado. Volviendo al menú...\n')
            return None

        contrasena = maskpass.askpass(prompt='Contraseña (0 para volver): ', mask='*')
        if contrasena == '0':
            print('\nVolviendo al menú principal...\n')
            return None

        usuario = autenticar_usuario(correo, contrasena)
        if usuario:
            print(f'\nBienvenido/a, {usuario.nombre} {usuario.apellido} [{usuario.rol}]\n')
            return usuario

        intentos += 1
        restantes = intentos_maximos - intentos
        print(f'\nContraseña incorrecta. Intentos restantes: {restantes}\n')

    print('Ha superado el número máximo de intentos. Volviendo al menú...\n')
    return None