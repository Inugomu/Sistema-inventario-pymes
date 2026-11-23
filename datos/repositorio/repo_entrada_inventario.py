from datos.modelos.entrada_inventario import EntradaInventario
from auxiliares.datos_inventario import mensaje_error

def listado_entradas():
    try:
        entradas = EntradaInventario.select()
        if entradas:
            return list(entradas)
    except Exception as error:
        print(f'{mensaje_error}: {error}')
        return []

def obtener_entrada_por_nombre(nombre_entrada):
    try:
        entrada = EntradaInventario.get(EntradaInventario.nombre == nombre_entrada)
        if entrada:
            return entrada
    except Exception as error:
        print(f'{mensaje_error}: {error}')
        return None

def guardar_entrada(entrada: EntradaInventario):
    try:
        respuesta = entrada.save()
        if respuesta == 1:
            print(f'Se ha guardado con éxito: {entrada.entrada}')
            return entrada
    except Exception as error:
        print(f'{mensaje_error}: {error}')
        return None
    