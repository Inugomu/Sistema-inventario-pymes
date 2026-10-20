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

def obtener_entrada_por_id(id_movimiento):
    try:
        return EntradaInventario.get(EntradaInventario.id_movimiento == id_movimiento)
    except Exception as error:
        print(f'{mensaje_error}: {error}')
        return None

def guardar_entrada(entrada: EntradaInventario):
    try:
        respuesta = entrada.save(force_insert=True)
        if respuesta == 1:
            print(f'Se ha guardado la entrada para el movimiento ID: {entrada.id_movimiento}')
            return entrada
    except Exception as error:
        print(f'{mensaje_error}: {error}')
        return None