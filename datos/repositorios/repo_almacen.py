from datos.modelos.almacen import Almacen

def listado_almacenes():
    almacenes = Almacen.select()
    if almacenes:
        return almacenes
    