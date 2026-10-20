from prettytable import PrettyTable
from datos.repositorios.repo_movimiento_inventario import listado_movimientos
from datos.repositorios.repo_producto import listado_productos

def procesar_listado_movimientos(tabla: PrettyTable):
    if tabla is not None:
        tabla.field_names = ['ID', 'Fecha', 'Tipo', 'Cantidad', 'Producto', 'Observación']
        movimientos = listado_movimientos()
        productos = {p.id_producto: p.nombre for p in listado_productos()} if listado_productos() else {}
        
        if movimientos:
            for mov in movimientos:
                nombre_prod = productos.get(mov.id_producto, f"ID {mov.id_producto}")
                tabla.add_row([
                    mov.id_movimiento,
                    mov.fecha,
                    mov.tipo_movimiento,
                    mov.cantidad,
                    nombre_prod,
                    mov.observacion if mov.observacion else 'Sin obs.'
                ])
            return tabla
    return None