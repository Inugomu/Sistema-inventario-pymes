from prettytable import PrettyTable
from auxiliares.datos_inventario import mensaje_error
from negocio.negocio_movimiento import procesar_listado_movimientos, registrar_movimiento_stock
from negocio.negocio_producto import procesar_listado_productos, obtener_tabla_proveedores

def mostrar_listado_movimientos():
    try:
        tabla_movimientos = PrettyTable()
        tabla_resultado = procesar_listado_movimientos(tabla_movimientos)
        if tabla_resultado:
            print('\n--- LISTADO DE MOVIMIENTOS DE INVENTARIO ---')
            print(tabla_resultado)
            print()
        else:
            print('\nNo hay movimientos registrados en la base de datos.\n')
    except Exception as error:
        print(f'{mensaje_error}: {error}')

def registrar_movimiento_inventario():
    print('\n=== ACTUALIZAR STOCK (ENTRADA / SALIDA) ===')
    tabla_prod = procesar_listado_productos(PrettyTable())
    if not tabla_prod:
        print('No hay productos registrados.\n')
        return

    print(tabla_prod)
    try:
        id_producto = int(input('Ingrese el ID del producto: ').strip())
    except ValueError:
        print('ID inválido.\n')
        return

    print('\nTipo de movimiento: [1] ENTRADA (Sumar stock)   [2] SALIDA (Descontar stock)')
    tipo_op = input('Seleccione opción [1-2]: ').strip()
    if tipo_op not in ['1', '2']:
        print('Opción inválida.\n')
        return

    try:
        cantidad = int(input('Cantidad de unidades: ').strip())
    except ValueError:
        print('La cantidad debe ser un número entero.\n')
        return

    observacion = input('Observación (ej. Reposición semanal / Venta mostrador): ').strip()

    if tipo_op == '1':
        tabla_prov, ids_prov = obtener_tabla_proveedores()
        print('\nProveedores:')
        print(tabla_prov)
        try:
            id_prov = int(input('ID del proveedor que entrega: ').strip())
            if id_prov not in ids_prov:
                print('Proveedor no válido.\n')
                return
        except ValueError:
            print('ID inválido.\n')
            return
        registrar_movimiento_stock(id_producto, 'ENTRADA', cantidad, observacion, id_prov)
    else:
        motivo = input('Motivo de salida (ej. Venta mostrador / Merma / Uso interno): ').strip()
        registrar_movimiento_stock(id_producto, 'SALIDA', cantidad, observacion, motivo)
    print()