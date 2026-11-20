from prettytable import PrettyTable
from auxiliares.datos_inventario import mensaje_error
from negocio.negocio_almacen import (
    procesar_listado_almacenes,
    almacen_por_id,
    crear_objeto_almacen,
    modificar_objeto_almacen,
    deshabilitar_objeto_almacen
)

def mostrar_listado_almacenes():
    try:
        tabla_almacenes = PrettyTable()
        tabla_resultado = procesar_listado_almacenes(tabla_almacenes)
        if tabla_resultado:
            print('\n--- LISTADO DE ALMACENES ---')
            print(tabla_resultado)
            print()
        else:
            print('\nNo hay almacenes para mostrar.\n')
    except Exception as error:
        print(f'{mensaje_error}: {error}')

def registrar_nuevo_almacen():
    print('\n=== REGISTRAR NUEVO ALMACÉN ===')
    nombre = input('Nombre del almacén: ').strip()
    if not nombre:
        print('El nombre es obligatorio.\n')
        return
    direccion = input('Dirección (opcional): ').strip()
    try:
        capacidad = int(input('Capacidad máxima (unidades): ').strip())
        if capacidad < 0:
            print('La capacidad no puede ser negativa.\n')
            return
    except ValueError:
        print('La capacidad debe ser un número entero.\n')
        return

    crear_objeto_almacen(nombre, direccion, capacidad)
    print()

def modificar_almacen():
    print('\n=== MODIFICAR ALMACÉN ===')
    mostrar_listado_almacenes()
    try:
        id_alm = int(input('Ingrese ID del almacén a modificar: ').strip())
    except ValueError:
        print('ID inválido.\n')
        return

    almacen = almacen_por_id(id_alm)
    if not almacen:
        print('Almacén no encontrado.\n')
        return

    print(f'Editando: {almacen.nombre_almacen}\n')
    nuevo_nombre = input('Nuevo Nombre (ENTER para conservar): ').strip()
    nueva_dir = input('Nueva Dirección (ENTER para conservar): ').strip()
    cap_str = input('Nueva Capacidad Máxima (ENTER para conservar): ').strip()
    nueva_cap = None
    if cap_str != '':
        try:
            nueva_cap = int(cap_str)
        except ValueError:
            print('Capacidad inválida. Operación cancelada.\n')
            return

    modificar_objeto_almacen(nuevo_nombre, nueva_dir, nueva_cap, almacen)
    print()

def eliminar_almacen():
    print('\n=== ELIMINAR ALMACÉN ===')
    mostrar_listado_almacenes()
    try:
        id_alm = int(input('Ingrese ID del almacén a eliminar: ').strip())
    except ValueError:
        print('ID inválido.\n')
        return

    almacen = almacen_por_id(id_alm)
    if not almacen:
        print('Almacén no encontrado.\n')
        return

    confirm = input(f'¿Seguro que desea eliminar "{almacen.nombre_almacen}"? [S/N]: ').strip().lower()
    if confirm == 's':
        deshabilitar_objeto_almacen(almacen)
    else:
        print('Operación cancelada.')
    print()