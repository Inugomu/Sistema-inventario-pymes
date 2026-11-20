from prettytable import PrettyTable
from datos.modelos.producto import Producto
from datos.modelos.producto_perecible import ProductoPerecible
from datos.modelos.producto_no_perecible import ProductoNoPerecible
from datos.repositorios.repo_producto import listado_productos, guardar_producto
from datos.repositorios.repo_categoria import listado_categorias
from datos.repositorios.repo_proveedor import listado_proveedores
from auxiliares.datos_inventario import mensaje_error

def procesar_listado_productos(tabla: PrettyTable):
    if tabla is not None:
        tabla.field_names = ['ID', 'Nombre', 'Precio', 'Stock Actual', 'Stock Mínimo', 'Estado Stock', 'Tipo']
        productos = listado_productos()
        if productos:
            for prod in productos:
                estado = '⚠️ BAJO STOCK' if prod.stock_actual <= prod.stock_minimo else 'OK'
                tabla.add_row([
                    prod.id_producto,
                    prod.nombre,
                    f"${prod.precio:,.0f}",
                    prod.stock_actual,
                    prod.stock_minimo,
                    estado,
                    prod.tipo_producto
                ])
            return tabla
    return None

def obtener_tabla_categorias():
    categorias = listado_categorias()
    if not categorias:
        return None, []
    tabla = PrettyTable(['ID', 'Categoría'])
    ids = []
    for c in categorias:
        tabla.add_row([c.id_categoria, c.nombre_categoria])
        ids.append(c.id_categoria)
    return tabla, ids

def obtener_tabla_proveedores():
    proveedores = listado_proveedores()
    if not proveedores:
        return None, []
    tabla = PrettyTable(['ID', 'Proveedor', 'Teléfono'])
    ids = []
    for p in proveedores:
        tabla.add_row([p.id_proveedor, p.nombre, p.telefono or 'N/A'])
        ids.append(p.id_proveedor)
    return tabla, ids

def crear_objeto_producto(nombre, descripcion, precio, stock_inicial, stock_minimo, tipo_producto, id_categoria, id_proveedor, dato_extra):
    try:
        prod = Producto()
        prod.nombre = nombre
        prod.descripcion = descripcion
        prod.precio = precio
        prod.stock_actual = stock_inicial
        prod.stock_minimo = stock_minimo
        prod.tipo_producto = tipo_producto
        prod.id_categoria = id_categoria
        prod.id_proveedor = id_proveedor
        
        guardado = guardar_producto(prod)
        if guardado:
            if tipo_producto == 'PERECIBLE':
                perecible = ProductoPerecible(id_producto=guardado.id_producto, fecha_vencimiento=dato_extra)
                perecible.save(force_insert=True)
            else:
                no_perecible = ProductoNoPerecible(id_producto=guardado.id_producto, garantia_meses=int(dato_extra))
                no_perecible.save(force_insert=True)
        return guardado
    except Exception as error:
        print(f'{mensaje_error}: {error}')
        return None
    