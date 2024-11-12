from views.menu_basico_view import menu_basico_view
from views.inversor.inversor_registrar_view import inversor_registrar_view
from views.inversor.inversor_login_view import inversor_login_view
from views.inversor.inversor_recuperar_contrasena_view import inversor_recuperar_contrasena_view
from utils.exit_program import exit_program

def mostrar_menu_principal_view(): 
    
    
    menu_principal_title = "Menú principal"
    menu_principal_opciones = {
        "1": ("Registrar inversor", inversor_registrar_view),
        "2": ("Login inversor", inversor_login_view),
        "3": ("Recuperar contraseña", inversor_recuperar_contrasena_view),
        "4": ("Cerrar programa", exit_program),
    }

    menu_basico_view(menu_principal_title, menu_principal_opciones)
