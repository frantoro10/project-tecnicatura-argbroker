# Este archivo gestiona la conexión a la base de datos utilizando mysql.connector y los datos de configuración almacenados en config.ini.
# Está diseñado para ser reutilizable, y es aquí donde se lee el archivo config.ini para obtener la información de conexión.

import mysql.connector
from mysql.connector import errorcode
import configparser
import pathlib



""" Nota: Agregado manejo de error adicional + Cierre de conexión """

class DBConn:
    def __init__(self, config_file="config.ini"):
        self.config_file = config_file

        if self.config_file:
            config = configparser.ConfigParser()
            config_path = pathlib.Path(__file__).parent.parent / config_file
            config.read(config_path)
            if 'database' not in config:
                raise ValueError("La configuración de la base de datos no está presente en el archivo de configuración.")
            self.db_config = config['database']
    
    def get_database_name(self):
        return self.db_config.get('database')

    def connect_to_mysql(self):
        try: 
            connection = mysql.connector.connect(
                user=self.db_config.get('user'),
                password=self.db_config.get('password'),
                host=self.db_config.get('host'),
                database=self.db_config.get('database')
            )
            return connection
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                raise ValueError("Usuario o Password no válido")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                raise ValueError("La base de datos no existe.")
            else:
                raise ValueError(f"Error al conectar a la base de datos: {err}")
        return None

    def close_connection(self, connection):
        if connection.is_connected():
            connection.close()

    #Metodos especiales para el bloque with que se usara en (DAO). Esto mejora la gestión de conexiones de MySQL, siempre cerrando la conexión al terminar el bloque with.
    def __enter__(self):
        # Cuando se entra en el bloque `with`, se abre la conexión
        self.connection = self.connect_to_mysql()
        return self.connection  # El objeto que se devolverá y usará dentro del bloque
    
    def __exit__(self, exc_type, exc_value, traceback):
    # Cuando se sale del bloque `with`, se cierra la conexión
        if self.connection:
            self.connection.close()

