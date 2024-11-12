class Accion:
    def __init__(self, id_accion: int, id_empresa: int, id_cotizacion: int, nombre_accion: str, precio_historico: float, fecha_actualizacion: str, cantidad_mercado: int):
        self.id_accion = id_accion
        self.id_empresa = id_empresa
        self.id_cotizacion = id_cotizacion
        self.nombre_accion = nombre_accion
        self.precio_historico = precio_historico
        self.fecha_actualizacion = fecha_actualizacion
        self.cantidad_mercado = cantidad_mercado
