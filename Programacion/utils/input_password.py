import readchar

def input_password(msj):
    print(msj, end='', flush=True)  # Muestra el mensaje sin saltar de línea
    password = ""
    while True:
        char = readchar.readchar()  # Lee un solo carácter
        if char == '\r' or char == '\n':  # Finaliza con Enter
            break
        elif char == '\x08' or char == '\x7f':  # Captura la tecla Backspace
            if len(password) > 0:
                password = password[:-1]
                print('\b \b', end='', flush=True)  # Borra el último asterisco
        else:
            password += char
            print('*', end='', flush=True)  # Muestra un asterisco por cada carácter
    print()  # Salta a la siguiente línea después de ingresar la contraseña
    return password