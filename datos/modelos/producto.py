class Producto:
    def __init__(self, id_producto, nombre, descripcion, precio, stock_actual, stock_minimo, tipo_producto, id_categoria, id_proveedor):
        self.__id_producto = id_producto
        self.__nombre = nombre
        self.__descripcion = descripcion
        self.__precio = precio
        self.__stock_actual = stock_actual
        self.__stock_minimo = stock_minimo
        self.__tipo_producto = tipo_producto
        self.__id_categoria = id_categoria
        self.__id_proveedor = id_proveedor