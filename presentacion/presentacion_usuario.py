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
    autenticar_usuario
)

def solicitar_rut(prompt, opcional=False):
    while True:
        rut = input(prompt).strip()
        if opcional and rut == '':
            return ''
        rut_valido, mensaje = validar_rut(rut)
        print(mensaje)
        if rut_valido != '':
            return rut_valido

def solicitar_texto(prompt, largo=50, opcional=False):
    while True:
        valor = input(prompt).strip()
        if opcional and valor == '':
            return ''
        valor_valido, mensaje = validar_largo_string(valor, largo)
        print(mensaje)
        if valor_valido != '':
            return valor_valido

def solicitar_correo(prompt, opcional=False):
    while True:
        correo = input(prompt).strip()
        if opcional and correo == '':
            return ''
        correo_valido, mensaje = validar_correo(correo)
        print(mensaje)
        if correo_valido != '':
            return correo_valido

def solicitar_rol(opcional=False):
    while True:
        print('Roles disponibles: [1] ADMINISTRADOR  [2] OPERADOR')
        opcion = input('Seleccione rol (ENTER para conservar/por defecto): ').strip()
        if opcional and opcion == '':
            return ''
        if opcion == '1':
            return 'ADMINISTRADOR'
        if opcion == '2' or opcion == '':
            return 'OPERADOR'
        print('Opción inválida.\n')

def solicitar_contrasena_segura(prompt):
    while True:
        print('\nRequisitos de contraseña:')
        print('- Entre 8 y 15 caracteres')
        print('- Al menos 1 mayúscula, 1 minúscula y 1 número')
        print('- Al menos 1 símbolo: !@#$%&/')
        contrasena = maskpass.askpass(prompt=prompt, mask='*')
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
    rut = solicitar_rut('RUT (ej. 12.345.678-9): ')
    nombre = solicitar_texto('Nombre: ', largo=50)
    apellido = solicitar_texto('Apellido: ', largo=50)
    correo = solicitar_correo('Correo electrónico: ')
    
    if es_registro_publico:
        rol = 'OPERADOR'
    else:
        rol = solicitar_rol()
        
    contrasena = solicitar_contrasena_segura('Contraseña: ')

    crear_objeto_usuario(rut, nombre, apellido, correo, contrasena, rol)
    print()

def modificar_usuario():
    print('\n=== MODIFICAR USUARIO ===')
    rut_buscar = solicitar_rut('Ingrese RUT del usuario a modificar: ')
    usuario = usuario_por_rut(rut_buscar)
    if not usuario:
        print('Usuario no encontrado.\n')
        return

    print(f'Editando a: {usuario.nombre} {usuario.apellido} ({usuario.correo})\n')
    nuevo_rut = solicitar_rut('Nuevo RUT (ENTER para conservar): ', opcional=True)
    nuevo_nombre = solicitar_texto('Nuevo Nombre (ENTER para conservar): ', largo=50, opcional=True)
    nuevo_apellido = solicitar_texto('Nuevo Apellido (ENTER para conservar): ', largo=50, opcional=True)
    nuevo_correo = solicitar_correo('Nuevo Correo (ENTER para conservar): ', opcional=True)
    nuevo_rol = solicitar_rol(opcional=True)

    modificar_objeto_usuario(nuevo_rut, nuevo_nombre, nuevo_apellido, nuevo_correo, nuevo_rol, usuario)
    print()

def eliminar_usuario():
    print('\n=== ELIMINAR (DESHABILITAR) USUARIO ===')
    rut_buscar = solicitar_rut('Ingrese RUT del usuario a eliminar: ')
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

    print('====================================')
    print('  INICIO DE SESIÓN - INVENTARIO PYME')
    print('====================================')

    while intentos < intentos_maximos:
        correo = solicitar_correo('Correo: ')
        contrasena = maskpass.askpass(prompt='Contraseña: ', mask='*')

        usuario = autenticar_usuario(correo, contrasena)
        if usuario:
            print(f'\nBienvenido/a, {usuario.nombre} {usuario.apellido} [{usuario.rol}]\n')
            return usuario

        intentos += 1
        restantes = intentos_maximos - intentos
        print(f'\nCredenciales incorrectas o usuario deshabilitado. Intentos restantes: {restantes}\n')

    print('Ha superado el número máximo de intentos. Cerrando sistema...')
    return None