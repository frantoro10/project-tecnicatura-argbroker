class Portafolio:
    def __init__(self,
                 id_usuario: int,
                 id_accion: int,
                 cantidad_acciones: int,
                 valor_comprometido: float,
                 rendimiento_operacion: float,
                 id_portafolio: int = None):
        self.id_portafolio = id_portafolio
        self.id_usuario = id_usuario
        self.id_accion = id_accion
        self.cantidad_acciones = cantidad_acciones
        self.valor_comprometido = valor_comprometido
        self.rendimiento_operacion = rendimiento_operacion
