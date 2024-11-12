from utils.loggin_colors import log_error

class Sql_Query():
    def __init__(self, db_conn=None):
        self.db_conn = db_conn
        
    def __set_query(self, query, data=None, fetchall=False, fetchone=False):
        try:
            with self.db_conn as connection:  
                cursor = connection.cursor()
                cursor.execute(query, data or ())
                result = None

                if fetchall and fetchone:
                    raise ValueError("No se puede usar fetchall y fetchone simultáneamente.")

                if fetchall:
                    result = cursor.fetchall()
                elif fetchone:
                    result = cursor.fetchone()
                if query.strip().upper().startswith(("INSERT", "UPDATE", "DELETE")):
                    connection.commit()
            return result
        

        except Exception as e:
            log_error(f"Error al ejecutar consulta: {e}")
            raise
        finally:
            if cursor:
                cursor.close()

    def get_one(self, query, data = None):
        return self.__set_query(query, data, fetchone=True)

    def get_all(self, query, data = None):
        return self.__set_query(query, data, fetchall=True)

    def execute(self, query, data = None):
        """INSERT, UPDATE, DELETE."""
        self.__set_query(query, data)