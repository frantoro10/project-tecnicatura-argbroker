from dao.interface_dao import DataAccessDAO
from models.portafolio import Portafolio
from utils.db_conn import DBConn

from utils.loggin_colors import log_error, log_info, log_warning
from utils.sql_query import Sql_Query

class PortafolioDAO(DataAccessDAO):
    def __init__(self, db_conn=None, sql_query=None):
        self.db_conn = db_conn or DBConn()
        self.sql_query = sql_query or Sql_Query(self.db_conn)
    
    def get(self, id):
        query = "SELECT * FROM portafolio WHERE id_usuario = %s"
        try:
            result = self.sql_query.get_all(query, (id,))
            if result:
                portafolios = []
                for item in result:
                    portafolio = Portafolio(
                        id_usuario=item[1],
                        id_accion=item[2],
                        cantidad_acciones=item[3],
                        valor_comprometido=item[4],
                        rendimiento_operacion=item[5],
                        id_portafolio=item[0]
                    )
                    portafolios.append(portafolio)
                   
                return portafolios
            else:
                return None
        except Exception as e:
            log_error(f"Error: {e}")
            return None
        
    
    def get_all(self):
        pass

 
    def create(self, portafolio):
        query = f"INSERT INTO {self.db_conn.get_database_name()}.portafolio (id_usuario, id_accion, cantidad_acciones, valor_comprometido, rendimiento_operacion) VALUES (%s, %s, %s, %s, %s)"
        data = (portafolio.id_usuario, portafolio.id_accion, portafolio.cantidad_acciones, portafolio.valor_comprometido, portafolio.rendimiento_operacion)
        try:
            self.sql_query.execute(query, data)
            log_info(f"Portafolio creado con éxito.")
        except Exception as e:
            log_error(f"Error al crear portafolio: {e}")
        

    def update(self, portafolio):
        query = f"""
                    UPDATE {self.db_conn.get_database_name()}.portafolio 
                    SET id_accion = %s, cantidad_acciones = %s, valor_comprometido = %s, rendimiento_operacion = %s
                    WHERE id_usuario = %s AND id_portafolio = %s
                """
        
        data = (
                        portafolio.id_portafolio,
                        portafolio.id_usuario,
                        portafolio.id_accion,
                        portafolio.cantidad_acciones,
                        portafolio.valor_comprometido,
                        portafolio.rendimiento_operacion
                    )
        try:
            self.sql_query.execute(query, data)
            log_info(f"Datos actualizados")
        except Exception as e:
            log_error(f"Error al intentar actualizar los datos: {e}")
        

    def delete(self, object):
        pass