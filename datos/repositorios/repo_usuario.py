from datos.modelos.usuario import Usuario
from auxiliares.datos_inventario import mensaje_error

def listado_usuarios_habilitados():
    try:
        usuarios = Usuario.select().where(Usuario.habilitado == 1)
        if usuarios:
            return list(usuarios)
    except Exception as error:
        print(f'{mensaje_error}: {error}')
        return []

def obtener_usuario_rut(rut_usuario):
    try:
        return Usuario.select().where(Usuario.rut == rut_usuario).first()
    except Exception as error:
        print(f'{mensaje_error}: {error}')
        return None

def obtener_usuario_correo(correo_usuario, solo_habilitados=True):
    try:
        if solo_habilitados:
            return Usuario.select().where(
                (Usuario.correo == correo_usuario) & (Usuario.habilitado == 1)
            ).first()
        return Usuario.select().where(Usuario.correo == correo_usuario).first()
    except Exception as error:
        print(f'{mensaje_error}: {error}')
        return None

def guardar_usuario(usuario: Usuario):
    try:
        respuesta = usuario.save()
        if respuesta == 1:
            print(f'Se ha guardado con éxito al usuario: {usuario.nombre} {usuario.apellido}')
            return usuario
    except Exception as error:
        print(f'{mensaje_error}: {error}')
        return None