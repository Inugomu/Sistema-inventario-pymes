CREATE DATABASE inventario_pyme;
USE inventario_pyme;

-- 1. CATEGORIA
CREATE TABLE categoria (
    id_categoria     INT AUTO_INCREMENT PRIMARY KEY,
    nombre_categoria VARCHAR(100) NOT NULL
);

-- 2. PROVEEDOR
CREATE TABLE proveedor (
    id_proveedor INT AUTO_INCREMENT PRIMARY KEY,
    nombre       VARCHAR(100) NOT NULL,
    telefono     VARCHAR(20),
    email        VARCHAR(100)
);

-- 3. ALMACEN
CREATE TABLE almacen (
    id_almacen       INT AUTO_INCREMENT PRIMARY KEY,
    nombre_almacen   VARCHAR(100) NOT NULL,
    direccion        VARCHAR(150),
    capacidad_maxima INT
);

-- 4. PRODUCTO
CREATE TABLE producto (
    id_producto   INT AUTO_INCREMENT PRIMARY KEY,
    nombre        VARCHAR(100) NOT NULL,
    descripcion   VARCHAR(255),
    precio        DECIMAL(10,2) NOT NULL,
    stock_actual  INT NOT NULL DEFAULT 0,
    stock_minimo  INT NOT NULL DEFAULT 0,
    tipo_producto ENUM('PERECIBLE', 'NO_PERECIBLE') NOT NULL,
    id_categoria  INT NOT NULL,
    id_proveedor  INT NOT NULL
);

-- 5. PRODUCTO_PERECIBLE
CREATE TABLE producto_perecible (
    id_producto       INT PRIMARY KEY,
    fecha_vencimiento DATE NOT NULL
);

-- 6. PRODUCTO_NO_PERECIBLE
CREATE TABLE producto_no_perecible (
    id_producto    INT PRIMARY KEY,
    garantia_meses INT NOT NULL DEFAULT 0
);

-- 7. PRODUCTO_ALMACEN
CREATE TABLE producto_almacen (
    id_registro  INT AUTO_INCREMENT PRIMARY KEY,
    id_producto  INT NOT NULL,
    id_almacen   INT NOT NULL,
    cantidad     INT NOT NULL DEFAULT 0
);

-- 8. MOVIMIENTO_INVENTARIO
CREATE TABLE movimiento_inventario (
    id_movimiento   INT AUTO_INCREMENT PRIMARY KEY,
    fecha           DATE NOT NULL,
    cantidad        INT NOT NULL,
    observacion     VARCHAR(255),
    tipo_movimiento ENUM('ENTRADA', 'SALIDA') NOT NULL,
    id_producto     INT NOT NULL
);

-- 9. ENTRADA_INVENTARIO
CREATE TABLE entrada_inventario (
    id_movimiento INT PRIMARY KEY,
    id_proveedor  INT NOT NULL
);

-- 10. SALIDA_INVENTARIO
CREATE TABLE salida_inventario (
    id_movimiento INT PRIMARY KEY,
    motivo_salida VARCHAR(150)
);
