from datetime import datetime
from prettytable import PrettyTable
from datos.modelos.movimiento_inventario import MovimientoInventario
from datos.modelos.entrada_inventario import EntradaInventario
from datos.modelos.salida_inventario import SalidaInventario
from datos.repositorio.repo_movimiento_inventario import listado_movimientos, guardar_movimiento
from datos.repositorio.repo_producto import listado_productos, obtener_producto_id, guardar_producto
from auxiliares.datos_inventario import mensaje_error

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

def registrar_movimiento_stock(id_producto: int, tipo_movimiento: str, cantidad: int, observacion: str, detalle_extra):
    try:
        producto = obtener_producto_id(id_producto)
        if not producto:
            print('El producto seleccionado no existe.')
            return None

        if cantidad <= 0:
            print('La cantidad debe ser mayor a 0.')
            return None

        if tipo_movimiento == 'SALIDA' and producto.stock_actual < cantidad:
            print(f'Stock insuficiente. Stock disponible de "{producto.nombre}": {producto.stock_actual} unidades.')
            return None

        # 1. Guardar movimiento base
        mov = MovimientoInventario()
        mov.fecha = datetime.now().date()
        mov.cantidad = cantidad
        mov.observacion = observacion
        mov.tipo_movimiento = tipo_movimiento
        mov.id_producto = id_producto
        mov_guardado = guardar_movimiento(mov)

        if mov_guardado:
            # 2. Guardar detalle según tipo y actualizar stock
            if tipo_movimiento == 'ENTRADA':
                entrada = EntradaInventario(id_movimiento=mov_guardado.id_movimiento, id_proveedor=int(detalle_extra))
                entrada.save(force_insert=True)
                producto.stock_actual += cantidad
            else:
                salida = SalidaInventario(id_movimiento=mov_guardado.id_movimiento, motivo_salida=detalle_extra)
                salida.save(force_insert=True)
                producto.stock_actual -= cantidad

            guardar_producto(producto)
            print(f'Nuevo stock de "{producto.nombre}": {producto.stock_actual} unidades.')
            return mov_guardado
    except Exception as error:
        print(f'{mensaje_error}: {error}')
        return None