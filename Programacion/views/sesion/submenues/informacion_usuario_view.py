import os
from views.menu_basico_view import menu_basico_view


menu = {
    "1": ("Cambiar contraseña", None),
    "2": ("Cambiar pin", None),
    "3": ("Volver al panel de control", False),
}

def informacion_usuario_view():
    print(f"""
            Nombre y apellido: {os.getenv('nombre_inversor')} {os.getenv('apellido_inversor')}
            Correo: {os.getenv('correo_inversor')}
            CUIL: {os.getenv('cuil_inversor')}
            Fecha de registro: {os.getenv('fecha_registro_inversor')}
        """)
    menu_basico_view("Opciones", menu)

    
