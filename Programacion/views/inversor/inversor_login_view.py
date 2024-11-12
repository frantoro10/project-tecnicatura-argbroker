from dao.inversor_dao import InversorDAO
import os
from utils.input_password import input_password

def login(dao, intentos_maximos):
    for intento in range(intentos_maximos):
            correo = input("Ingrese su correo: ")
            contrasena = input_password("Ingrese su contraseña: ")
            user = dao.get_login(correo, contrasena)
            if user:
                return user
            elif intento == intentos_maximos - 1:
                return None
            else:
                print(f"El correo o contraseña no osn correctos, intente nuevamente.\nQuedan {intentos_maximos - intento - 1} intentos.\n")
        

def inversor_login_view():
    dao = InversorDAO()
    while True:
        intentos_maximos = 3

        user = login(dao, intentos_maximos)

        if user:    
            # Creamos las variables de entorno
            os.environ['id_inversor'] = str(user.id_usuario)
            os.environ['nombre_inversor'] = user.nombre
            os.environ['apellido_inversor'] = user.apellido
            os.environ['saldo_inversor'] = str(user.saldo)
            os.environ['correo_inversor'] = user.correo
            os.environ['pin_inversor'] = str(user.pin)
            os.environ['cuil_inversor'] = str(user.cuil)
            os.environ['fecha_registro_inversor'] = str(user.fecha_registro)
            return  

        
        else:
            print(f"Se ha excedido el número de intentos para iniciar sesión.\n")
            return
            







