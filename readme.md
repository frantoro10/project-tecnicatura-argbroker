
# ARGBroker - README

# English:
## Purpose

The ARGBroker application for stock investment allows users to invest and perform buy/sell stock transactions efficiently. It is designed to simulate a basic investment system, providing a simple and accessible user experience for those who wish to manage and visualize their assets and stock transactions.

## Context

This project is a learning exercise in console application development, designed to consolidate knowledge in Python, relational database management (MySQL), design patterns such as DAO (Data Access Object), and PEP 8 naming conventions. The application was developed in an educational environment to demonstrate how to integrate a simple and solid backend with a functional console interface, allowing the registration and management of user and investment data.

## Scope

The application covers the following key functionalities:

#### User Management:
Users can register, log in, and recover passwords. User profile information is stored and managed.

#### Stock Purchase and Sale Transactions:
Investors can choose from a list of available stocks to buy and manage the stocks they own to sell, with a commission percentage applied to each transaction.

#### Portfolio Visualization: 
Users can view the stocks in their portfolio with detailed information such as the number of shares and their current value.

#### Database Connection: 
The application uses a MySQL database to securely store all user and transaction information, with CRUD operations implemented using the DAO pattern.

This project is limited to console data handling and does not include a graphical user interface. Transactions are simulated without any connection to real stock markets.

## Installation and Usage 

#### Requirements:

- Python 3.x  
- MySQLConnector (check `requirements.txt`)

#### Setup:

- Clone the repository.  
- Create a database in MySQL, run the table creation script (`arg_broker.sql`), and execute the `data_mock` script to insert sample data.  
- Configure the connection credentials in the `config.ini` file to enable the connection via `db_conn` located in the `utils` folder.

#### Execution:

From the terminal, run:
python main.py

## Project Structure
#### models:
Contains the data model classes.

#### dao:
Implements the DAO design pattern to handle data connection and manipulation.

#### views:
Contains the views that present user options and manage the console interface.

#### utils:
Includes utilities such as the database connection (db_conn).

#### main.py: Main file to run the application.



# Spanish:

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



