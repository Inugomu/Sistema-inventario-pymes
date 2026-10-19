from datos.modelos.categoria import categoria
from auxiliares import mensaje_error

def listado_categorias():
    try:
        categorias = Categoria.select()
        if categorias:
            return categorias
    except Exception as error:
        print(f'{mensaje_error}{error}')

def obtener_categoria_nombre(nombre_categoria):
    try:
        categoria = Categoria.get(Categoria.categoria == nombre_categoria)
        if categoria:
            return categoria
    except Exception as error:
        print(f'Ha ocurrido un error: {error}')

def guardar_categoria(categoria:Categoria):
    try:
        respuesta = categoria.save()
        if respuesta == 1:
            print(f'{mensaje_error}{categoria.categoria}')
    except Exception as error:
        print(f'{mensaje_error}{error}')

