import bcrypt
from datetime import datetime
from prettytable import PrettyTable
from datos.modelos.usuario import Usuario
from datos.repositorio.repo_usuario import (
    listado_usuarios_habilitados,
    obtener_usuario_rut,
    obtener_usuario_correo,
    guardar_usuario
)
from auxiliares.datos_inventario import mensaje_error

def procesar_listado_usuarios(tabla: PrettyTable):
    if tabla is not None:
        tabla.field_names = ['ID', 'RUT', 'Nombre Completo', 'Correo', 'Rol', 'Incorporación', 'Estado']
        usuarios = listado_usuarios_habilitados()
        if usuarios:
            for u in usuarios:
                nombre_completo = f'{u.nombre} {u.apellido}'
                estado = 'Habilitado' if u.habilitado else 'Deshabilitado'
                tabla.add_row([
                    u.id_usuario,
                    u.rut,
                    nombre_completo,
                    u.correo,
                    u.rol,
                    u.fecha_incorporacion,
                    estado
                ])
            return tabla
    return None

def crear_objeto_usuario(rut: str, nombre: str, apellido: str, correo: str, contrasena_plana: str, rol: str = 'OPERADOR'):
    try:
        hash_bytes = bcrypt.hashpw(contrasena_plana.encode('utf-8'), bcrypt.gensalt())
        usuario = Usuario()
        usuario.rut = rut
        usuario.nombre = nombre.title()
        usuario.apellido = apellido.title()
        usuario.correo = correo.lower()
        usuario.password = hash_bytes.decode('utf-8')
        usuario.rol = rol.upper()
        usuario.fecha_incorporacion = datetime.now().date()
        usuario.habilitado = 1
        return guardar_usuario(usuario)
    except Exception as error:
        print(f'{mensaje_error}: {error}')
        return None

def modificar_objeto_usuario(rut: str, nombre: str, apellido: str, correo: str, rol: str, usuario: Usuario):
    try:
        if rut and usuario.rut != rut:
            usuario.rut = rut
        if nombre and usuario.nombre != nombre:
            usuario.nombre = nombre.title()
        if apellido and usuario.apellido != apellido:
            usuario.apellido = apellido.title()
        if correo and usuario.correo != correo:
            usuario.correo = correo.lower()
        if rol and usuario.rol != rol:
            usuario.rol = rol.upper()
        return guardar_usuario(usuario)
    except Exception as error:
        print(f'{mensaje_error}: {error}')
        return None

def deshabilitar_objeto_usuario(usuario: Usuario):
    try:
        usuario.habilitado = 0
        return guardar_usuario(usuario)
    except Exception as error:
        print(f'{mensaje_error}: {error}')
        return None

def usuario_por_rut(rut: str):
    return obtener_usuario_rut(rut)

def usuario_por_correo(correo: str):
    return obtener_usuario_correo(correo.lower(), solo_habilitados=False)

def autenticar_usuario(correo: str, contrasena_plana: str):
    try:
        usuario = obtener_usuario_correo(correo.lower(), solo_habilitados=True)
        if not usuario:
            return None
        password_guardada = usuario.password.encode('utf-8')
        if bcrypt.checkpw(contrasena_plana.encode('utf-8'), password_guardada):
            return usuario
        return None
    except Exception as error:
        print(f'{mensaje_error}: {error}')
        return None