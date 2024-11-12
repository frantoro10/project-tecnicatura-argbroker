
#Modelamos entidad Inversor - Usuario
class Inversor:
    def __init__(self, nombre: str, apellido: str, cuil: int, correo: str, contrasena: str, pin: int, saldo:float, id_usuario: int = None, fecha_registro: str = None):
        self.nombre = nombre
        self.apellido = apellido
        self.cuil = cuil
        self.correo = correo
        self.contrasena = contrasena
        self.pin = pin
        self.saldo = saldo      
        self.id_usuario = id_usuario
        self.fecha_registro = fecha_registro

    def __str__(self):
        return f"Control de datos: id:{self.id_usuario}, nombre y apellido: {self.nombre} {self.apellido}, CUIL: {self.cuil}, Correo: {self.correo}, Saldo: {self.saldo},Inicio: {self.fecha_registro}"

