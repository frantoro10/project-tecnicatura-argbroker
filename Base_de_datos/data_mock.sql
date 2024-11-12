
INSERT INTO usuarios (id_usuario, cuil, nombre, apellido, correo, contrasena, pin, saldo, fecha_registro) VALUES
('1', '20348537808', 'Juan', 'Cabalango', 'juancabalango01@gmail.com', '12345', '345', 1000000.00,'2024-05-20 10:54:34'),
('2','23234567281', 'Ariel', 'Marquez',  'marquezariel@outlook.com', '37582', '582', 1000000.00, '2024-07-21 11:24:54'),
('3','27358394562', 'Marta', 'Albanesi', 'marta_albanesi@gmai.com', '843956', '956', 1000000.00, '2024-08-19 03:45:04'),
('4','20385475724', 'Fabricio', 'Tello',  'fabricio.tello@gmail.com', '18456', '456', 1000000.00, '2024-05-02 12:27:11'),
('5','27438574859', 'Elena', 'Murciel',  'elenamurciel.ok@outlook.com', '90453', '453', 1000000.00, '2024-02-16 07:07:07'),
('6','23248573012', 'Tamara', 'Camino',  'caminotamara02@gmail.com', '47538', '538', 1000000.00, '2024-03-04 02:43:12'),
('7', '23418483729', 'Roberto', 'Vega',  'vega_roberto@gmail.com', '84637', '637', 1000000.00, '2024-04-29 05:12:57'),
('8','27479227324', 'Lisa', 'Mandorian',  'lisamandorian2011@gmail.com', '37459', '459', 1000000.00, '2024-02-22 06:23:34'),
('9','20383446331', 'Federico', 'Prado',  'fedeprado@gmail.com', '85432', '432', 1000000.00, '2024-01-31 11:54:34'),
('10','23157383325', 'Ana', 'Lobos',  'ana_lobos.01@gmail.com', '47384', '384', 1000000.00, '2024-09-19 05:22:07');

INSERT INTO empresas (id_empresa, nombre_empresa) VALUES 
('1', 'Arcor'), 
('2', 'Google'), 
('3', 'Meta'), 
('4', 'Banco Macro'), 
('5', 'Libertad SRL'), 
('6', 'Grupo Financiero Galicia'), 
('7', 'Metrogas'), 
('8', 'Telecom Argentina'), 
('9', 'YPF'), 
('10', 'Grupo Superville');

INSERT INTO cotizacion (id_cotizacion, precio_compra, precio_venta, fecha_cotizacion) VALUES 
('1', '824.82', '822.82', '2024-10-25 11:10:45'),
('2', '934.35', '925.77', '2024-10-25 11:10:45'),
('3', '1134.23', '1124.56', '2024-10-25 11:10:45'),
('4', '2845.78', '2825.78', '2024-10-25 11:10:45'),
('5', '5678.55', '5658.35', '2024-10-25 11:10:45'),
('6', '10465.33', '10405.23', '2024-10-25 11:10:45'),
('7', '9234.44', '9212.34', '2024-10-25 11:10:45'),
('8', '67734.00', '67687.00', '2024-10-25 11:10:45'),
('9', '223.82', '213.82', '2024-10-25 11:10:45'),
('10', '7765.99', '7754.82', '2024-10-25 11:10:45');

INSERT INTO acciones (id_accion, id_empresa, id_cotizacion, nombre_accion, precio_historico, fecha_actualizacion, cantidad_mercado)
VALUES 
('1' ,'1' ,'1' ,'Accion_Arcor', 800.00, '2024-10-20 11:11:59',10),
('2' ,'2' ,'2' ,'Accion_Google', 900.00, '2024-10-20 11:11:59',23),
('3' ,'3' ,'3' ,'Accion_Meta', 11000.00, '2024-10-20 11:11:59',65),
('4' ,'4' ,'4' ,'Accion_BancoMacro', 28000.00, '2024-10-20 11:11:59',87),
('5' ,'5' ,'5' ,'Accion_LibertadSRL', 5600.00, '2024-10-20 11:11:59',34),
('6' ,'6' ,'6' ,'Accion_GrupoFinancieroGalicia', 10400.00, '2024-10-20 11:11:59',84),
('7' ,'7' ,'7' ,'Accion_Metrogas', 9200.00, '2024-10-20 11:11:59',12),
('8' ,'8' ,'8' ,'Accion_TelecomArgentina', 67600.00, '2024-10-20 11:11:59',65),
('9' ,'9' ,'9' ,'Accion_YPF', 200.00, '2024-10-20 11:11:59',43),
('10' ,'10' ,'10' ,'Accion_GrupoSuperville', 7700.00, '2024-10-20 11:11:59',76);

INSERT INTO transacciones (id_transaccion, id_usuario, id_accion, id_cotizacion, tipo_operacion, cantidad, precio_unitario, total_operacion, broker_comision, fecha_transaccion)
VALUES
('1', '1', '1', '1', 'compra', 50, 822.82, 41141.00, 1.5, '2024-10-25 11:10:45'),
('2', '1', '2', '2', 'compra', 30, 925.77, 27773.10, 1.5, '2024-10-26 11:10:45'),
('3', '2', '3', '3', 'venta', 20, 1124.56, 22491.20, 1.5, '2024-10-26 12:15:30'),
('4', '3', '4', '4', 'compra', 10, 2825.78, 28257.80, 1.5, '2024-10-27 09:00:00'),
('5', '4', '5', '5', 'venta', 5, 5658.35, 28291.75, 1.5, '2024-10-27 10:05:15');

INSERT INTO portafolio (id_portafolio, id_usuario, id_accion, cantidad_acciones, valor_comprometido, rendimiento_operacion) VALUES 
('1', '1', '1', 50, 41141.00, 1000.00), 
('2', '1', '2', 30, 27773.10, 500.00),
('3', '2', '3', 20, 22491.20, 800.00),
('4', '3', '4', 10, 28257.80, 1200.00),
('5', '4', '5', 5, 28291.75, 600.00);

-- Consultas UPDATE
UPDATE usuarios SET saldo = saldo + 5000.00 WHERE id_usuario = 1;
UPDATE empresas SET nombre_empresa = 'Grupo Arcor' WHERE id_empresa = 1;
UPDATE cotizacion SET precio_compra = 830.00 WHERE id_cotizacion = 1;
UPDATE acciones SET precio_historico = 820.00 WHERE id_accion = 1;
UPDATE transacciones SET total_operacion = total_operacion * 1.02 WHERE id_transaccion = 1;

-- Consultas SELECT
SELECT * FROM usuarios;
SELECT * FROM empresas;
SELECT * FROM cotizacion;
SELECT * FROM acciones;
SELECT * FROM transacciones;

-- Consultas Multitabla

-- Queremos conocer el historial de transacciones del usuario con ID 1 para evaluar su rendimiento.
SELECT t.id_transaccion, t.tipo_operacion, t.cantidad, t.precio_unitario, t.total_operacion, a.nombre_accion 
FROM transacciones t 
JOIN acciones a ON t.id_accion = a.id_accion 
WHERE t.id_usuario = 1;


-- Queremos saber el saldo y las acciones en el portafolio de cada usuario.
SELECT u.nombre, u.apellido, u.saldo, a.nombre_accion, p.cantidad_acciones 
FROM usuarios u 
JOIN portafolio p ON u.id_usuario = p.id_usuario 
JOIN acciones a ON p.id_accion = a.id_accion;


-- Queremos calcular el rendimiento total de las transacciones de cada usuario para evaluar su desempeño en el mercado.
SELECT u.nombre, u.apellido, SUM(t.total_operacion) AS rendimiento_total 
FROM usuarios u 
JOIN transacciones t ON u.id_usuario = t.id_usuario 
GROUP BY u.id_usuario;
