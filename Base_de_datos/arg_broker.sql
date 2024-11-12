CREATE DATABASE IF NOT EXISTS Arg_broker;

USE Arg_broker; 

-- TABLA Usuarios 
CREATE TABLE IF NOT EXISTS usuarios 
(
    id_usuario INT AUTO_INCREMENT PRIMARY KEY,
    cuil VARCHAR (11) NOT NULL UNIQUE,
    nombre VARCHAR (50) NOT NULL,
    apellido VARCHAR (50) NOT NULL,
    correo VARCHAR (100) NOT NULL UNIQUE,
    contrasena VARCHAR (100) NOT NULL, 
    pin VARCHAR (4) NOT NULL,
    saldo DECIMAL (15,2),
    fecha_registro TIMESTAMP DEFAULT CURRENT_TIMESTAMP    
);

-- TABLA Empresas
CREATE TABLE IF NOT EXISTS empresas 
(
    id_empresa INT AUTO_INCREMENT PRIMARY KEY,
    nombre_empresa VARCHAR (100) NOT NULL
);

-- TABLA Cotizacion

CREATE TABLE IF NOT EXISTS cotizacion
(
    id_cotizacion INT AUTO_INCREMENT PRIMARY KEY,
    precio_compra DECIMAL (10,2) NOT NULL, 
    precio_venta DECIMAL (10,2) NOT NULL,
    fecha_cotizacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP 
);

-- TABLA Acciones

CREATE TABLE IF NOT EXISTS acciones 
(
    id_accion INT AUTO_INCREMENT PRIMARY KEY,
    id_empresa INT, 
    id_cotizacion INT, 
    nombre_accion VARCHAR (100) NOT NULL, 
    precio_historico DECIMAL (15,2) NOT NULL,
    fecha_actualizacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    cantidad_mercado INT NOT NULL,
    FOREIGN KEY (id_empresa) REFERENCES empresas (id_empresa),
    FOREIGN KEY (id_cotizacion) REFERENCES cotizacion (id_cotizacion)
);

-- TABLA Transacciones

CREATE TABLE IF NOT EXISTS transacciones 
(
    id_transaccion INT AUTO_INCREMENT PRIMARY KEY,
    id_usuario INT,
    id_accion INT,
    id_cotizacion INT,
    tipo_operacion ENUM ('compra', 'venta') NOT NULL,
    cantidad INT NOT NULL,
    precio_unitario DECIMAL (10,2) NOT NULL,
    total_operacion DECIMAL (15,2) NOT NULL,
    broker_comision DECIMAL(10,1) DEFAULT 1.5,
    fecha_transaccion TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (id_usuario) REFERENCES usuarios (id_usuario),
    FOREIGN KEY (id_accion) REFERENCES acciones (id_accion),
    FOREIGN KEY (id_cotizacion) REFERENCES cotizacion (id_cotizacion)
);


-- TABLA Portafolio 

CREATE TABLE IF NOT EXISTS portafolio 
(
    id_portafolio INT AUTO_INCREMENT PRIMARY KEY,
    id_usuario INT,
    id_accion INT,
    cantidad_acciones INT NOT NULL,
    valor_comprometido DECIMAL (15,2) NOT NULL,
    rendimiento_operacion DECIMAL (15,2) NOT NULL,
    FOREIGN KEY (id_usuario) REFERENCES usuarios (id_usuario),
    FOREIGN KEY (id_accion) REFERENCES acciones (id_accion)
);


    
