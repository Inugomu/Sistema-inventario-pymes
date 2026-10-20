from datos.modelos.categoria import Categoria
from auxiliares.datos_inventario import mensaje_error

def listado_categorias():
    try:
        categorias = Categoria.select()
        if categorias:
            return list(categorias)
    except Exception as error:
        print(f'{mensaje_error}: {error}')
        return []

def obtener_categoria_nombre(nombre_categoria):
    try:
        return Categoria.get(Categoria.nombre_categoria == nombre_categoria)
    except Exception as error:
        print(f'{mensaje_error}: {error}')
        return None

def guardar_categoria(categoria: Categoria):
    try:
        respuesta = categoria.save()
        if respuesta == 1:
            print(f'Se ha guardado la categoría: {categoria.nombre_categoria}')
            return categoria
    except Exception as error:
        print(f'{mensaje_error}: {error}')
        return None