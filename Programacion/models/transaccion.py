class Transaccion:
    def __init__(self, id_transaccion: int, id_usuario: int, id_accion: int, id_cotizacion: int, tipo_operacion: str, cantidad: int, precio_unitario: float, total_operacion: float, fecha_transaccion: str, broker_comision: float = 1.5):
        self.id_transaccion = id_transaccion
        self.id_usuario = id_usuario
        self.id_accion = id_accion
        self.id_cotizacion = id_cotizacion
        self.tipo_operacion = tipo_operacion
        self.cantidad = cantidad
        self.precio_unitario = precio_unitario
        self.total_operacion = total_operacion
        self.fecha_transaccion = fecha_transaccion
        self.broker_comision = broker_comision


    
