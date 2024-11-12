
""" 
Fore: BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET.
Back: BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET.
Style: DIM, NORMAL, BRIGHT, RESET_ALL

Fore: LIGHTBLACK_EX, LIGHTRED_EX, LIGHTGREEN_EX, LIGHTYELLOW_EX, LIGHTBLUE_EX, LIGHTMAGENTA_EX, LIGHTCYAN_EX, LIGHTWHITE_EX
Back: LIGHTBLACK_EX, LIGHTRED_EX, LIGHTGREEN_EX, LIGHTYELLOW_EX, LIGHTBLUE_EX, LIGHTMAGENTA_EX, LIGHTCYAN_EX, LIGHTWHITE_EX

"""

import logging
from colorama import Fore, init, Style

logging.basicConfig(level=logging.DEBUG, format=f'\n%(levelname)s: %(message)s\n')

init(autoreset=True)

def log_color(color, message):
    text = color + message + Style.RESET_ALL
    return text

            
def log_error(message):
    logging.error(log_color(Fore.RED, message))

def log_info(message):
    logging.info(log_color(Fore.LIGHTBLUE_EX, message))

def log_warning(message):
    logging.warning(log_color(Fore.LIGHTRED_EX, message))





