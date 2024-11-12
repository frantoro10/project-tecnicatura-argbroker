
# ARGBroker - README

## Proposito

La aplicación ARGBroker para la inversión de Acciones, permite a los usuarios invertir y realizar transacciones de compra y venta de acciones de manera eficiente. Está diseñada para simular un sistema de inversión básico, proporcionando una experiencia de usuario sencilla y accesible para quienes deseen administrar y visualizar sus activos y transacciones de acciones.

## Contexto
Este proyecto es un ejercicio de aprendizaje en el desarrollo de aplicaciones de consola, diseñado para consolidar los conocimientos en Python, manejo de bases de datos relacionales (MySQL), patrones de diseño como el DAO (Data Access Object) y las convenciones de nomenclatura PEP 8. La aplicación fue desarrollada en un entorno educativo para demostrar cómo integrar un backend simple y sólido con una interfaz de consola funcional, permitiendo el registro y la gestión de datos de usuarios e inversiones.

## Alcance
La aplicación cubre las siguientes funcionalidades clave:

 #### Gestión de Usuarios:
  Los usuarios pueden registrarse, iniciar sesión, y recuperar contraseñas. Se almacena y maneja información de perfil de usuario.

 ####  Transacciones de Compra y Venta de Acciones:
  Permite a los inversores seleccionar entre un listado de acciones disponibles para comprar y gestionar las acciones que poseen para vender, con un porcentaje de comisión aplicado a cada transacción.

 #### Visualización de Portafolio: 
 Los usuarios pueden ver las acciones en su portafolio con información detallada como la cantidad de acciones y su valor actual.

 #### Conexión con Base de Datos: 
 La aplicación utiliza una base de datos MySQL para almacenar de manera segura toda la información de usuarios y transacciones, con operaciones CRUD implementadas en el patrón DAO.

Este proyecto está limitado al manejo de datos en consola y no incluye una interfaz gráfica. Las transacciones se simulan sin conexión a mercados de valores reales.

## Instalación y Uso 
#### Requisitos:

Python 3.x
MySQLConnector(consultar requirements.txt)
#### Configuración:

Clonar el repositorio.
Crear una base de datos en MySQL, ejecutar el script de creación de tablas (archivo arg_broker.sql) y ejecutar script (data_mock) para insertar los datos.
Configurar las credenciales de conexión en el archivo config.ini para realizar la conexión con db_conn de la carpeta utils.
#### Ejecución:

Desde la terminal, ejecutar python main.py para iniciar la aplicación.

## Estructura del proyecto
#### models: 
Contiene las clases del modelo de datos.
#### dao: 
Implementa el patrón de diseño DAO para manejar la conexión y manipulación de datos.
#### views: 
Contiene las vistas que presentan opciones al usuario y manejan la interfaz de consola.
#### utils: 
Incluye utilidades como la conexión a la base de datos (db_conn).
main.py: Archivo principal para ejecutar la aplicación.



