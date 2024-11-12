from dao.interface_dao import DataAccessDAO
from models.inversor import Inversor
from utils.db_conn import DBConn

from utils.loggin_colors import log_error, log_info, log_warning
from utils.sql_query import Sql_Query

class InversorDAO(DataAccessDAO):
    def __init__(self, db_conn=None, sql_query=None):
        self.db_conn = db_conn or DBConn()
        self.sql_query = sql_query or Sql_Query(self.db_conn)

    def __map_result_to_inversor(self, result):
        return Inversor(
                        id_usuario=result[0],
                        nombre=result[1],
                        apellido=result[2],
                        cuil=result[3],
                        correo=result[4],
                        contrasena=result[5],
                        pin=result[6],
                        saldo=result[7],
                        fecha_registro=result[8]
                   )


    def create(self, inversor):
        query = f"""
            INSERT INTO {self.db_conn.get_database_name()}.usuarios 
            (nombre, apellido, cuil, correo, contrasena, pin, saldo) 
            VALUES (%s, %s, %s, %s, %s, %s, %s);
        """
        data = (inversor.nombre, inversor.apellido, inversor.cuil, inversor.correo, inversor.contrasena, inversor.pin, inversor.saldo)
        try:
            self.sql_query.execute(query, data)
            log_info(f"Inversor {inversor.nombre} {inversor.apellido} registrado con éxito.")
        except Exception as e:
            log_error(f"Error al registrar inversor: {e}")     
            

    def get(self, id):
        pass


    def get_all(self):
        query = f"""
            SELECT id_usuario, cuil, nombre, apellido, correo, contrasena, pin, saldo, fecha_registro 
            FROM {self.db_conn.get_database_name()}.usuarios
        """
        results = self.sql_query.get_all(query)
        return [self.__map_result_to_inversor(result) for result in results] if results else []

            

    def update(self, inversor):
        query = f"""
            UPDATE {self.db_conn.get_database_name()}.usuarios 
            SET nombre = %s, apellido = %s, cuil = %s, correo = %s, contrasena = %s, pin = %s
            WHERE id_usuario = %s
        """
        data = (
            inversor.nombre, inversor.apellido, inversor.cuil, inversor.correo,
            inversor.contrasena, inversor.pin, inversor.saldo, inversor.id_usuario
        )
        try:
            self.sql_query.execute(query, data)
            log_info("Datos actualizados")
        except Exception as e:
            log_error(f"Error al intentar actualizar los datos: {e}")



    def delete(self, inversor):
        query = f"DELETE FROM {self.db_conn.get_database_name()}.usuarios WHERE id_usuario = %s"
        data = (inversor.id_usuario,)
        try:
            self.sql_query.execute(query, data)
            log_info(f"Inversor {inversor.nombre} {inversor.apellido} eliminado con éxito.")
        except Exception as e:
            log_error(f"Error al intentar eliminar inversor: {e}")


    """  Métodos exclusivos de clase InversorDAO """
    
    
    def get_login(self, correo, contrasena):
        query = f"SELECT id_usuario, nombre, apellido, cuil, correo, contrasena, pin, saldo, fecha_registro FROM {self.db_conn.get_database_name()}.usuarios WHERE correo = %s AND contrasena = %s"
        data = (correo, contrasena)
        try:
            result = self.sql_query.get_one(query, data)
            if result:
                inversor = self.__map_result_to_inversor(result)
                log_info(f"Inversor {inversor.nombre} {inversor.apellido} ha iniciado sesión con éxito.")
                return inversor
            else:
                log_warning(f"Intento de inicio de sesión fallido para el correo: {correo}")
                return None
        except Exception as e:
            log_error(f"Error al intentar iniciar sesión: {e}")
            return None
        

    def get_verificar_usuario(self, correo, pin):
        query = f"SELECT correo FROM {self.db_conn.get_database_name()}.usuarios WHERE correo = %s AND pin = %s"
        data = (correo, pin)
        try:
            usuario_existe = self.sql_query.get_one(query, data)
            if not usuario_existe:
                return False
            return True
        except Exception as e:
            log_error(f"Error al verificar el usuario: {e}")
            return False


    def set_contrasena_nueva(self, correo, contrasena_nueva):
        query = f"UPDATE {self.db_conn.get_database_name()}.usuarios SET contrasena = %s WHERE correo = %s"
        data = (contrasena_nueva, correo)
        try:
            self.sql_query.execute(query, data)
            log_info(f"Contraseña de {correo} actualizada con éxito.")
        except Exception as e:
          log_error(f"Error al intentar actualizar la contraseña: {e}")

    
    def get_saldo(self, id_usuario):
        query = f"SELECT saldo FROM {self.db_conn.get_database_name()}.usuarios WHERE id_usuario = %s"
        data = (id_usuario,)
        try:
            saldo = self.sql_query.get_one(query, data)
            return saldo[0] if saldo else None
        except Exception as e:
            log_error(f"Error al obtener el saldo: {e}")
            return None