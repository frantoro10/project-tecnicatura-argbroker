from dao.interface_dao import DataAccessDAO
from utils.db_conn import DBConn

from utils.loggin_colors import log_error, log_info, log_warning
from utils.sql_query import Sql_Query


class TransaccionDAO(DataAccessDAO):
    def __init__(self, db_conn=None, sql_query=None):
        self.db_conn = db_conn or DBConn()
        self.sql_query = sql_query or Sql_Query(self.db_conn)
    
    def get(self, id: int):
        pass
 
    def get_all(self):
        pass

    def create(self, object):
        pass

    def update(self, object):
        pass

    def delete(self, object):
        pass
 
    def comprar_accion(self, id_usuario, id_accion, cantidad):
        try:
            with DBConn() as connection:
                
                with connection.cursor() as cursor:
                    cursor.execute("SELECT saldo FROM usuarios WHERE id_usuario = %s", (id_usuario,))
                    saldo_actual = cursor.fetchone()
                    if saldo_actual is None:
                        raise ValueError("El usuario no tiene un saldo disponible.")
                    saldo_actual = saldo_actual[0]

                    cursor.execute("SELECT broker_comision FROM transacciones")
                    result = cursor.fetchall()
                    comision_broker = result[0][0] if result else 0.015

                    cursor.execute("""
                        SELECT c.precio_compra, a.id_cotizacion 
                        FROM acciones a 
                        JOIN cotizacion c ON a.id_cotizacion = c.id_cotizacion 
                        WHERE a.id_accion = %s
                    """, (id_accion,))
                    precio_result = cursor.fetchone()
                    if precio_result is None:
                        raise ValueError("No se encontró la cotización para la acción solicitada.")
                    precio_compra, id_cotizacion = precio_result

                    total_operacion = precio_compra * cantidad
                    comision = total_operacion * comision_broker
                    costo_total = total_operacion + comision

                    if saldo_actual < costo_total:
                        log_warning("Saldo insuficiente para hacer la compra.")
                        return False

                    query_transaccion = """
                        INSERT INTO transacciones 
                        (id_usuario, id_accion, id_cotizacion, tipo_operacion, cantidad, precio_unitario, total_operacion, broker_comision) 
                        VALUES (%s, %s, %s, 'compra', %s, %s, %s, %s)
                    """
                    cursor.execute(query_transaccion, (id_usuario, id_accion, id_cotizacion, cantidad, precio_compra, costo_total, comision))

                    nuevo_saldo = saldo_actual - costo_total
                    cursor.execute("UPDATE usuarios SET saldo = %s WHERE id_usuario = %s", (nuevo_saldo, id_usuario))

                    cursor.execute("SELECT cantidad_acciones FROM portafolio WHERE id_usuario = %s AND id_accion = %s", (id_usuario, id_accion))
                    portafolio_result = cursor.fetchone()

                    if portafolio_result:
                        cantidad_actual = portafolio_result[0]
                        nueva_cantidad = cantidad_actual + cantidad
                        cursor.execute("UPDATE portafolio SET cantidad_acciones = %s WHERE id_usuario = %s AND id_accion = %s", (nueva_cantidad, id_usuario, id_accion))
                    else:
                        cursor.execute("""
                            INSERT INTO portafolio (id_usuario, id_accion, cantidad_acciones, valor_comprometido, rendimiento_operacion) 
                            VALUES (%s, %s, %s, %s, %s)
                        """, (id_usuario, id_accion, cantidad, costo_total, 0.0))

                    connection.commit()
                    log_info("Compra de acción realizada con éxito.")
                    return True

        except Exception as e:
            log_error(f"Error al realizar la compra de acción: {e}")
            return False
    
    def vender_accion(self, id_usuario, id_accion, cantidad):
        try:
            with DBConn() as connection:
                with connection.cursor() as cursor:
                    cursor.execute("SELECT cantidad_acciones FROM portafolio WHERE id_usuario = %s AND id_accion = %s", (id_usuario, id_accion))
                    portafolio_result = cursor.fetchone()

                    if portafolio_result is None:
                        log_warning("No se encontraron acciones en el portafolio para vender.")
                        return False
                    
                    cantidad_actual = portafolio_result[0]
                    if cantidad > cantidad_actual:
                        log_warning("No se puede vender más acciones de las que posee.")
                        return False

                    cursor.execute(""" 
                        SELECT c.precio_venta, a.id_cotizacion 
                        FROM acciones a 
                        JOIN cotizacion c ON a.id_cotizacion = c.id_cotizacion 
                        WHERE a.id_accion = %s
                    """, (id_accion,))
                    precio_result = cursor.fetchone()
                    if precio_result is None:
                        raise ValueError("No se encontró la cotización para la acción solicitada")
                    precio_venta, id_cotizacion = precio_result

                    precio_venta_float = float(precio_venta)

                    total_operacion = precio_venta_float * cantidad
                    comision_broker = 0.015
                    comision = total_operacion * comision_broker
                    ingreso_total = total_operacion - comision

                    query_transaccion = """
                        INSERT INTO transacciones 
                        (id_usuario, id_accion, id_cotizacion, tipo_operacion, cantidad, precio_unitario, total_operacion, broker_comision) 
                        VALUES (%s, %s, %s, 'venta', %s, %s, %s, %s)
                    """
                    cursor.execute(query_transaccion, (id_usuario, id_accion, id_cotizacion, cantidad, precio_venta, ingreso_total, comision))

                    nueva_cantidad = cantidad_actual - cantidad
                    if nueva_cantidad > 0:
                        cursor.execute("UPDATE portafolio SET cantidad_acciones = %s WHERE id_usuario = %s AND id_accion = %s", (nueva_cantidad, id_usuario, id_accion))
                    else:
                        cursor.execute("DELETE FROM portafolio WHERE id_usuario = %s AND id_accion = %s", (id_usuario, id_accion))

                    cursor.execute("UPDATE usuarios SET saldo = saldo + %s WHERE id_usuario = %s", (ingreso_total, id_usuario))

                    connection.commit()
                    log_info("Venta de acción realizada con éxito.")
                    return True

        except Exception as e:
            log_error(f"Error al realizar la venta de acción: {e}")
            return False
