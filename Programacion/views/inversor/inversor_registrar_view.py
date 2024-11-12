from dao.inversor_dao import InversorDAO
from models.inversor import Inversor
from utils.input_password import input_password

def inversor_registrar_view():
    nombre = input("Ingrese nombre: ")
    apellido = input("Ingrese apellido: ")
    cuil = input("Ingrese CUIL: ")
    correo = input("Ingrese email: ")
    contrasena = input_password("Ingrese contraseña: ")
    pin = input_password("Ingrese pin: ")
    saldo = 1000000.00

    inversor = Inversor(nombre, apellido, cuil, correo, contrasena, pin, saldo)
    dao = InversorDAO()
    dao.create(inversor)