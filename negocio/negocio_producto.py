from prettytable import PrettyTable
from datos.repositorios.repo_producto import listado_productos

def procesar_listado_productos(tabla: PrettyTable):
    if tabla is not None:
        tabla.field_names = ['ID', 'Nombre', 'Precio', 'Stock Actual', 'Stock Mínimo', 'Tipo']
        productos = listado_productos()
        if productos:
            for prod in productos:
                tabla.add_row([
                    prod.id_producto,
                    prod.nombre,
                    f"${prod.precio:,.2f}",
                    prod.stock_actual,
                    prod.stock_minimo,
                    prod.tipo_producto
                ])
            return tabla
    return None