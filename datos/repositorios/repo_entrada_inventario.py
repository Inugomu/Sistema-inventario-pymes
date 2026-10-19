from datos.modelos.entrada_inventaro import Entrada_inventario
from auxiliares import mensaje_error

def listado_entradas():
    try:
        entradas = Entrada.select()
        if entradas:
            return entradas
    except Exception as error:
        print(f'{mensaje_error}{error}')

def obtener_entrada_nombre(nombre_entrada):
    try:
        entrada = Entrada.get(Entrada.entrada == nombre_entrada)
        if entrada:
            return entrada
    except Exception as error:
        print(f'{mensaje_error}{error}')

def guardar_entrada(entrada:Entrada):
    try:
        respuesta = entrada.save()
        if respuesta == 1:
            print (f'Se ha guardado con éxito: {entrada.Entrada}')
    except Exception as error:
        print(f'{mensaje_error}{error}')

