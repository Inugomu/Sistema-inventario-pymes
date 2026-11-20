from datetime import datetime
from prettytable import PrettyTable
from auxiliares.datos_inventario import mensaje_error
from negocio.negocio_producto import (
    procesar_listado_productos,
    obtener_tabla_categorias,
    obtener_tabla_proveedores,
    crear_objeto_producto
)

def mostrar_listado_productos():
    try:
        tabla_productos = PrettyTable()
        tabla_resultado = procesar_listado_productos(tabla_productos)
        if tabla_resultado:
            print('\n--- LISTADO DE PRODUCTOS ---')
            print(tabla_resultado)
            print()
        else:
            print('\nNo hay productos registrados en el sistema.\n')
    except Exception as error:
        print(f'{mensaje_error}: {error}')

def registrar_nuevo_producto():
    print('\n=== REGISTRAR NUEVO PRODUCTO ===')
    nombre = input('Nombre del producto: ').strip()
    if not nombre:
        print('El nombre es obligatorio.\n')
        return

    descripcion = input('Descripción (opcional): ').strip()

    try:
        precio = float(input('Precio ($): ').strip())
        stock_inicial = int(input('Stock inicial: ').strip())
        stock_minimo = int(input('Stock mínimo de alerta: ').strip())
    except ValueError:
        print('Error: Precio y stocks deben ser valores numéricos.\n')
        return

    # Seleccionar Categoría
    tabla_cat, ids_cat = obtener_tabla_categorias()
    if not tabla_cat:
        print('No hay categorías registradas en la base de datos.\n')
        return
    print('\nCategorías disponibles:')
    print(tabla_cat)
    try:
        id_categoria = int(input('Seleccione ID de Categoría: ').strip())
        if id_categoria not in ids_cat:
            print('ID de categoría inválido.\n')
            return
    except ValueError:
        print('Debe ingresar un número.\n')
        return

    # Seleccionar Proveedor
    tabla_prov, ids_prov = obtener_tabla_proveedores()
    if not tabla_prov:
        print('No hay proveedores registrados en la base de datos.\n')
        return
    print('\nProveedores disponibles:')
    print(tabla_prov)
    try:
        id_proveedor = int(input('Seleccione ID de Proveedor: ').strip())
        if id_proveedor not in ids_prov:
            print('ID de proveedor inválido.\n')
            return
    except ValueError:
        print('Debe ingresar un número.\n')
        return

    # Tipo de producto (Perecible / No Perecible)
    print('\nTipo de Producto: [1] PERECIBLE   [2] NO PERECIBLE')
    opcion_tipo = input('Seleccione tipo [1-2]: ').strip()
    if opcion_tipo == '1':
        tipo_producto = 'PERECIBLE'
        fecha_str = input('Fecha de vencimiento [AAAA-MM-DD]: ').strip()
        try:
            dato_extra = datetime.strptime(fecha_str, '%Y-%m-%d').date()
        except ValueError:
            print('Formato de fecha inválido (use AAAA-MM-DD).\n')
            return
    elif opcion_tipo == '2':
        tipo_producto = 'NO_PERECIBLE'
        try:
            dato_extra = int(input('Meses de garantía (ej. 12): ').strip())
        except ValueError:
            print('Los meses de garantía deben ser un número entero.\n')
            return
    else:
        print('Tipo de producto inválido.\n')
        return

    crear_objeto_producto(
        nombre, descripcion, precio, stock_inicial,
        stock_minimo, tipo_producto, id_categoria, id_proveedor, dato_extra
    )
    print()
    