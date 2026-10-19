from datos.modelos.proveedor import proveedor
from auxiliares import mensaje_error

def listado_proveedores():
    try:
        proveedores = Proveedor.select()
        if provedores:
            return provedores
    except Exception as error:
        print(f'{mensaje_error}{error}')
    
def obtener_proveedor_nombre(nombre_proveedor):
    try:
        proveedor = Proveedor.get(Proveedor.proveedor == nombre_proveedor)
        if proveedor:
            return proveedor
    except Exception as error:
        print(f'{mensaje_error}{error}')

def guardar_proveedor(proveedor.Proveedor):
    try:
        respuesta == proveedor.save()
        if respuesta == 1:
            print(f'Se ha guardado con éxito: {proovedor.proveedor}')
    except Exception as error:
        print(f'{mensaje_error}{error}')

