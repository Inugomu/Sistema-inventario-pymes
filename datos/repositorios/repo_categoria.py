from datos.modelos.categoria import Categoria
from auxiliares.datos_inventario import mensaje_error

def listado_categorias():
    try:
        categorias = Categoria.select()
        if categorias:
            return categorias
    except Exception as error:
        print(f'{mensaje_error}: {error}')

def obtener_categoria_nombre(nombre_categoria):
    try:
        categoria = Categoria.get(Categoria.nombre == nombre_categoria)
        if categoria:
            return categoria
    except Exception as error:
        print(f'{mensaje_error}: {error}')

def guardar_categoria(categoria: Categoria):
    try:
        respuesta = categoria.save()
        if respuesta == 1:
            print(f'Se ha guardado con éxito: {categoria.categoria}')
    except Exception as error:
        print(f'{mensaje_error}: {error}')
