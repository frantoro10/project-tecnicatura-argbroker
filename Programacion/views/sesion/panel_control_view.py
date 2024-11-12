# Diseñar menú de panel control: usuario, saldo actual o inicial, transacciones, historial de transacciones, Inversiones, Portafolio, Ayuda
from views.menu_basico_view import menu_basico_view
from views.sesion.submenues.informacion_usuario_view import informacion_usuario_view
from views.sesion.submenues.transacciones_view import transacciones_view
from views.sesion.submenues.portafolio_view import portafolio_view
from views.sesion.submenues.ayuda_view import ayuda_view
from views.inversor.inversor_cerrar_sesion_view import inversor_cerrar_sesion_view
from utils.exit_program import exit_program

def session_panel_control_view():
    menu_panel_control_title = "Menú principal"
    menu_panel_control_opciones = {
        "1": ("Información del usuario", informacion_usuario_view),
        "2": ("Transacciones", transacciones_view),
        "3": ("Portafolio", portafolio_view),
        "5": ("Ayuda", ayuda_view),
        "6": ("Cerrar sesión", inversor_cerrar_sesion_view),
        "7": ("Salir del programa", exit_program),
    }

    menu_basico_view(menu_panel_control_title, menu_panel_control_opciones)