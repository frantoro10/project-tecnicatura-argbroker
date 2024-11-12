from dao.inversor_dao import InversorDAO
from views.menu_basico_view import menu_basico_view
from utils.input_password import input_password


def recuperar_contrasena():
    dao = InversorDAO()
    
    intentos_maximos = 3
    for intento in range(intentos_maximos):
    
        correo = input("Ingrese su correo: ")
        pin = input_password("Ingrese su PIN: ")
        verificacion = dao.get_verificar_usuario(correo, pin)
        
        if verificacion:
            for intento_contrasena in range(intentos_maximos):
                
                contrasena_nueva = input_password("Ingrese la nueva contraseña: ")
                confirmar_contrasena_nueva = input_password("Confirme la nueva contraseña: ")
                if contrasena_nueva == confirmar_contrasena_nueva:
                    dao.set_contrasena_nueva(correo, contrasena_nueva)
                    return
                else:
                    print(f"Las contraseñas no coinciden, intente de nuevo.\nTe quedan {intentos_maximos - intento_contrasena - 1} intentos.\n")
            print("Se ha excedido el número de intentos para recuperar la contraseña.")
            return
        else:
            print(f"No se encontró un usuario con el correo {correo} y PIN {pin}\nTe quedan {intentos_maximos - intento - 1} intentos.\n")

    print("Se ha excedido el número de intentos para recuperar la contraseña.")
    return


recuperar_menu = {
    "1": ("Ingresar nueva contraseña", recuperar_contrasena),
    "2": ("Volver al menú principal", None)
}

def inversor_recuperar_contrasena_view():
    menu_basico_view("Quiero recuperar mi contraseña", recuperar_menu)