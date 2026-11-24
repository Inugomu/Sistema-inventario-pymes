from datos.repositorio.repo_almacen import listado_almacenes, obtener_almacen_nombre, guardar_almacen
from datos.repositorio.repo_categoria import listado_categorias, obtener_categoria_nombre, guardar_categoria
from datos.repositorio.repo_producto import listado_productos, obtener_producto_nombre, guardar_producto
from datos.repositorio.repo_proveedor import listado_proveedores, obtener_proveedor_nombre, guardar_proveedor
from datos.repositorio.repo_movimiento_inventario import listado_movimientos, guardar_movimiento
from datos.repositorio.repo_entrada_inventario import listado_entradas, guardar_entrada
from datos.repositorio.repo_salida_inventario import listado_salidas, guardar_salida
from datos.repositorio.repo_usuario import (
    listado_usuarios_habilitados,
    obtener_usuario_rut,
    obtener_usuario_correo,
    guardar_usuario
)