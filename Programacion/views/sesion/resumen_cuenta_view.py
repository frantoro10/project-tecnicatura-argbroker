# Crear interfaz de resumen: saldo inicial o actual, historial de transacciones y rendimiento de inversiones
import os
def resumen_cuenta_view():
    print(f"""Hola {os.getenv('nombre_inversor')} {os.getenv('apellido_inversor')}, este es tu resumen de cuenta:
          Saldo actual: ${os.getenv('saldo_inversor')}
          Rendimiento de inversions: 0%
          """)     