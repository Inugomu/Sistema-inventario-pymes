from prettytable import PrettyTable
from datos.repositorios.repo_movimiento_inventario import listado_movimientos
from datos.repositorios.repo_producto import listado_productos

def procesar_listado_movimientos(tabla: PrettyTable):
    if tabla is not None:
        tabla.field_names = ['ID', 'Fecha', 'Tipo', 'Cantidad', 'ID Producto', 'Observación']
        movimientos = listado_movimientos()
        
        if movimientos:
            for mov in movimientos:
                tabla.add_row([
                    mov.id_movimiento,
                    mov.fecha,
                    mov.tipo_movimiento,
                    mov.cantidad,
                    mov.id_producto,
                    mov.observacion if mov.observacion else 'Sin obs.'
                ])
            return tabla
    return None