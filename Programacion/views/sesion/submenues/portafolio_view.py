from dao.portafolio_dao import PortafolioDAO
from models.portafolio import Portafolio
from views.menu_basico_view import menu_basico_view
import os

def crear_portafolio():
    id_usuario = int(os.getenv("id_inversor"))
    print(f"Creando portafolio para el usuario con id: {id_usuario}")
    
    portafolio = Portafolio(id_usuario, None, 0, 0, 0)
    dao = PortafolioDAO()
    dao.create(portafolio)


def get_portafolio(id_usuario):
    dao = PortafolioDAO()
    portafolio = dao.get(id_usuario)
    return portafolio


def portafolio_view():
    id_usuario = int(os.getenv("id_inversor"))

    portafolio = get_portafolio(id_usuario)
    if portafolio:
        for item in portafolio:
            print(f"Acción número: {item.id_accion}, Cantidad: {item.cantidad_acciones}, Valor comprometido: {item.valor_comprometido}, Rendimiento de las operaciones: {item.rendimiento_operacion}")
        print("")
    else:
        portafolio = crear_portafolio()       
        portafolio = get_portafolio(id_usuario)
        print(f"""
        Portafolio:{portafolio}
        """)
    
 