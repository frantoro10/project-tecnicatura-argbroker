from utils.loggin_colors import log_info, log_warning
""" 
    
    INSTRUCCIONES DE USO

    titulo = ""
    opciones = {
        n : ("descripcion", funcion),
        ...
    }

    menu_basico(titulo, opciones)

"""

def menu_basico_view(menu_titulo, menu_options):
    msg_error = f"Opción no válida\nPor favor intente de nuevo\n"

    print(menu_titulo)
    for key, value in menu_options.items():
        print(f"{key}: {value[0]}")
    print("")

    opcion = None
    while opcion not in menu_options:
        opcion = input("Ingrese una opción: ").strip()
        if opcion.isdigit():
            break
        else:
            log_warning(msg_error)

    if opcion in menu_options:
        descripcion, funcion = menu_options[opcion]
        log_info(f"{descripcion}".upper())
        if funcion:
            funcion()
        
    else:
        log_warning(msg_error)