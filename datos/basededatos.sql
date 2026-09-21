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
-- ---------- 1. CATEGORIA  ----------
INSERT INTO categoria (nombre_categoria) VALUES
    ('Café en grano'),
    ('Café molido'),
    ('Lácteos'),
    ('Pastelería'),
    ('Panadería'),
    ('Bebidas frías'),
    ('Insumos desechables'),
    ('Jarabes y salsas'),
    ('Snacks'),
    ('Equipamiento de café');

-- ---------- 2. PROVEEDOR  ----------
INSERT INTO proveedor (nombre, telefono, email) VALUES
    ('Café Fantasía Ltda.', '+56912345678', 'contacto@cafefantasia.cl'),
    ('Distribuidora Lácteos Los Ríos', '+56923456789', 'ventas@lacteoslosrios.cl'),
    ('Panadería La Espiga', '+56934567890', 'pedidos@laespiga.cl'),
    ('Comercial Sur Insumos', '+56945678901', 'contacto@comercialsur.cl'),
    ('Nestlé Chile S.A.', '+56226123456', 'clientes@nestle.cl'),
    ('Colun', '+56642201000', 'ventas@colun.cl'),
    ('Agrícola San Pedro', '+56956789012', 'info@agricolasanpedro.cl'),
    ('Desechables Temuco Ltda.', '+56967890123', 'ventas@desechablestemuco.cl'),
    ('Barista Import SpA', '+56978901234', 'contacto@baristaimport.cl'),
    ('Frutos del Sur', '+56989012345', 'pedidos@frutosdelsur.cl');

-- ---------- 3. ALMACEN  ----------
INSERT INTO almacen (nombre_almacen, direccion, capacidad_maxima) VALUES
    ('Bodega Central', 'Av. Alemania 0671, Temuco', 500),
    ('Refrigerador Barra', 'Av. Alemania 0671, Temuco (interior local)', 100),
    ('Congelador Pastelería', 'Av. Alemania 0671, Temuco (interior local)', 80),
    ('Bodega Insumos Desechables', 'Av. Alemania 0671, Temuco (bodega trasera)', 300),
    ('Vitrina Pastelería', 'Av. Alemania 0671, Temuco (mesón principal)', 60),
    ('Bodega Seca', 'Av. Alemania 0671, Temuco (bodega trasera)', 250),
    ('Estante Café en Grano', 'Av. Alemania 0671, Temuco (barra)', 50),
    ('Bodega Envases', 'Av. Alemania 0671, Temuco (bodega trasera)', 400),
    ('Área Barista', 'Av. Alemania 0671, Temuco (barra)', 40),
    ('Bodega Sucursal Portal Temuco', 'Portal Temuco, Av. Alemania 671 local 15', 200);

-- ---------- 4. PRODUCTO ( 10 perecibles + 10 no perecibles) ----------
INSERT INTO producto (nombre, descripcion, precio, stock_actual, stock_minimo, tipo_producto, id_categoria, id_proveedor) VALUES
    ('Café en grano Colombia 1kg', 'Grano tostado origen Colombia', 12990.00, 30, 5, 'PERECIBLE', 1, 1),
    ('Café en grano Brasil 1kg', 'Grano tostado origen Brasil', 11990.00, 25, 5, 'PERECIBLE', 1, 1),
    ('Leche entera 1L', 'Leche entera pasteurizada', 1200.00, 60, 15, 'PERECIBLE', 3, 2),
    ('Leche descremada 1L', 'Leche descremada pasteurizada', 1250.00, 40, 10, 'PERECIBLE', 3, 2),
    ('Crema de leche 500ml', 'Crema para preparaciones', 2500.00, 20, 5, 'PERECIBLE', 3, 6),
    ('Croissant de mantequilla', 'Croissant artesanal', 1500.00, 24, 6, 'PERECIBLE', 4, 3),
    ('Muffin de arándano', 'Muffin relleno con arándanos', 1700.00, 18, 4, 'PERECIBLE', 4, 3),
    ('Pan de masa madre 500g', 'Pan artesanal de masa madre', 2200.00, 15, 3, 'PERECIBLE', 5, 3),
    ('Jugo natural de naranja 500ml', 'Jugo recién exprimido', 1800.00, 20, 5, 'PERECIBLE', 6, 10),
    ('Yogurt natural 1L', 'Yogurt natural sin azúcar', 2100.00, 15, 4, 'PERECIBLE', 3, 6),
    ('Café molido espresso 500g', 'Molienda fina para espresso', 6990.00, 40, 8, 'NO_PERECIBLE', 2, 1),
    ('Café molido descafeinado 500g', 'Molienda descafeinada', 7200.00, 15, 3, 'NO_PERECIBLE', 2, 1),
    ('Vaso desechable 12oz (x50)', 'Vasos de cartón para bebidas calientes', 5990.00, 30, 5, 'NO_PERECIBLE', 7, 8),
    ('Vaso desechable 16oz (x50)', 'Vasos de cartón para bebidas calientes', 6990.00, 25, 5, 'NO_PERECIBLE', 7, 8),
    ('Servilletas de papel (x100)', 'Paquete de servilletas', 1990.00, 50, 10, 'NO_PERECIBLE', 7, 8),
    ('Sirope de vainilla 750ml', 'Sirope saborizante para bebidas', 8990.00, 12, 3, 'NO_PERECIBLE', 8, 9),
    ('Sirope de caramelo 750ml', 'Sirope saborizante para bebidas', 8990.00, 12, 3, 'NO_PERECIBLE', 8, 9),
    ('Galletas integrales (caja x12)', 'Galletas para acompañar café', 3200.00, 20, 5, 'NO_PERECIBLE', 9, 5),
    ('Agua mineral con gas 500ml', 'Agua mineral embotellada', 900.00, 40, 10, 'NO_PERECIBLE', 6, 5),
    ('Filtro de papel para cafetera (x40)', 'Filtros desechables', 4500.00, 10, 2, 'NO_PERECIBLE', 10, 9);

-- ---------- 5. PRODUCTO_PERECIBLE (10, productos 1-10) ----------
INSERT INTO producto_perecible (id_producto, fecha_vencimiento) VALUES
    (1, '2027-03-01'),
    (2, '2027-02-15'),
    (3, '2026-09-20'),
    (4, '2026-09-18'),
    (5, '2026-09-25'),
    (6, '2026-09-08'),
    (7, '2026-09-08'),
    (8, '2026-09-10'),
    (9, '2026-09-15'),
    (10, '2026-09-30');

-- ---------- 6. PRODUCTO_NO_PERECIBLE (10, productos 11-20) ----------
INSERT INTO producto_no_perecible (id_producto, garantia_meses) VALUES
    (11, 12),
    (12, 12),
    (13, 24),
    (14, 24),
    (15, 36),
    (16, 18),
    (17, 18),
    (18, 8),
    (19, 12),
    (20, 24);

-- ---------- 7. PRODUCTO_ALMACEN (10) ----------
INSERT INTO producto_almacen (id_producto, id_almacen, cantidad) VALUES
    (1, 7, 15),
    (2, 7, 10),
    (3, 2, 20),
    (4, 2, 15),
    (6, 5, 12),
    (7, 5, 8),
    (11, 6, 25),
    (13, 8, 30),
    (16, 9, 6),
    (20, 1, 10);

-- ---------- 8. MOVIMIENTO_INVENTARIO ( 10 entradas + 10 salidas) ----------
INSERT INTO movimiento_inventario (fecha, cantidad, observacion, tipo_movimiento, id_producto) VALUES
    ('2026-08-01', 20, 'Reposición mensual café en grano Colombia', 'ENTRADA', 1),
    ('2026-08-01', 15, 'Reposición café en grano Brasil', 'ENTRADA', 2),
    ('2026-08-03', 40, 'Compra semanal de leche entera', 'ENTRADA', 3),
    ('2026-08-03', 30, 'Compra semanal de leche descremada', 'ENTRADA', 4),
    ('2026-08-05', 20, 'Entrega croissants panadería', 'ENTRADA', 6),
    ('2026-08-05', 15, 'Entrega muffins de arándano', 'ENTRADA', 7),
    ('2026-08-10', 30, 'Reposición café molido espresso', 'ENTRADA', 11),
    ('2026-08-12', 50, 'Compra vasos desechables 12oz', 'ENTRADA', 13),
    ('2026-08-15', 12, 'Compra sirope de vainilla', 'ENTRADA', 16),
    ('2026-08-18', 20, 'Compra filtros de papel', 'ENTRADA', 20),
    ('2026-09-01', 5, 'Venta mostrador café en grano', 'SALIDA', 1),
    ('2026-09-02', 8, 'Consumo leche para preparaciones', 'SALIDA', 3),
    ('2026-09-02', 6, 'Venta croissants del día', 'SALIDA', 6),
    ('2026-09-03', 4, 'Venta muffins del día', 'SALIDA', 7),
    ('2026-09-04', 10, 'Consumo café molido en barra', 'SALIDA', 11),
    ('2026-09-05', 15, 'Consumo vasos desechables', 'SALIDA', 13),
    ('2026-09-06', 3, 'Consumo sirope de vainilla', 'SALIDA', 16),
    ('2026-09-07', 5, 'Consumo filtros de papel', 'SALIDA', 20),
    ('2026-09-08', 6, 'Venta yogurt natural', 'SALIDA', 10),
    ('2026-09-09', 4, 'Venta jugo natural de naranja', 'SALIDA', 9);

-- ---------- 9. ENTRADA_INVENTARIO (10, movimientos 1-10) ----------
INSERT INTO entrada_inventario (id_movimiento, id_proveedor) VALUES
    (1, 1),
    (2, 1),
    (3, 2),
    (4, 2),
    (5, 3),
    (6, 3),
    (7, 1),
    (8, 8),
    (9, 9),
    (10, 9);

-- ---------- 10. SALIDA_INVENTARIO (10, movimientos 11-20) ----------
INSERT INTO salida_inventario (id_movimiento, motivo_salida) VALUES
    (11, 'Venta mostrador'),
    (12, 'Uso interno - preparación de bebidas'),
    (13, 'Venta mostrador'),
    (14, 'Venta mostrador'),
    (15, 'Uso interno - preparación de bebidas'),
    (16, 'Uso interno - servicio en barra'),
    (17, 'Uso interno - preparación de bebidas'),
    (18, 'Uso interno - preparación de café filtrado'),
    (19, 'Venta mostrador'),
    (20, 'Venta mostrador');
