# 📈 ARGBroker

## 🇬🇧 English Version

### 🎯 Purpose

**ARGBroker** is a console-based stock investment application that allows users to simulate **buying and selling stocks**, visualize their **portfolio**, and manage user accounts in a simple, educational environment.

---

### 🧠 Context

This project was created as a **learning exercise** to:

- Consolidate knowledge in **Python**  
- Work with **MySQL relational databases**  
- Apply the **DAO (Data Access Object)** design pattern  
- Follow **PEP8** code style conventions

It integrates a solid backend with a **functional console interface**, simulating real-world investment behavior.

---

### 🧩 Scope

The application includes the following core features:

#### 👤 User Management
- User registration and login  
- Password recovery  
- Profile data storage and handling  

#### 💸 Stock Transactions
- Purchase stocks from an available list  
- Sell owned stocks  
- Each transaction includes a **commission fee**

#### 📊 Portfolio Visualization
- View portfolio details  
- Includes current value, number of shares, and total investment

#### 🛢️ MySQL Database Integration
- All data is persisted using **MySQL**
- CRUD operations managed via **DAO pattern**

> ⚠️ This project simulates transactions and does **not connect to real stock markets**.  
> It is designed for console-based interactions only.

---

### 🧪 Installation & Usage

#### 📋 Requirements

- Python `3.x`  
- `mysql-connector-python` (Check `requirements.txt`)

#### ⚙️ Setup

1. Clone the repository  
2. Create a database in MySQL  
3. Run `arg_broker.sql` to create tables  
4. Run `data_mock.sql` to insert sample data  
5. Set your database credentials in `config.ini` (inside `/utils`)

#### ▶️ Run

```bash
python main.py
```

---

### 🗂️ Project Structure

```text
/dao       → DAO pattern for database access  
/models    → Data model classes  
/views     → Console interface logic  
/utils     → Utility functions and DB connection  
main.py    → Entry point of the application  
```

---

## 🇪🇸 Versión en Español

### 🎯 Propósito

**ARGBroker** es una aplicación de consola para inversión en acciones que permite simular **compras y ventas**, visualizar el **portafolio**, y gestionar cuentas de usuario de forma sencilla y educativa.

---

### 🧠 Contexto

Este proyecto fue desarrollado como un ejercicio para:

- Consolidar conocimientos en **Python**  
- Utilizar bases de datos relacionales con **MySQL**  
- Aplicar el patrón de diseño **DAO (Data Access Object)**  
- Seguir las convenciones de código **PEP8**

Integra un backend sólido con una **interfaz funcional por consola**.

---

### 🧩 Alcance

La aplicación incluye las siguientes funcionalidades clave:

#### 👤 Gestión de Usuarios
- Registro e inicio de sesión  
- Recuperación de contraseña  
- Almacenamiento de datos de perfil  

#### 💸 Transacciones de Acciones
- Comprar acciones disponibles  
- Vender acciones propias  
- Aplicación de un **porcentaje de comisión**

#### 📊 Visualización del Portafolio
- Visualización del portafolio con:
  - Cantidad de acciones  
  - Valor actual  
  - Inversión total

#### 🛢️ Conexión a Base de Datos
- Datos almacenados con **MySQL**
- Operaciones CRUD mediante el **patrón DAO**

> ⚠️ Este proyecto simula transacciones y **no se conecta a mercados reales**.  
> Funciona únicamente por consola.

---

### 🧪 Instalación y Uso

#### 📋 Requisitos

- Python `3.x`  
- `mysql-connector-python` (ver `requirements.txt`)

#### ⚙️ Configuración

1. Clonar el repositorio  
2. Crear una base de datos en MySQL  
3. Ejecutar `arg_broker.sql` para crear las tablas  
4. Ejecutar `data_mock.sql` para insertar datos de ejemplo  
5. Configurar las credenciales en `config.ini` (dentro de `/utils`)

#### ▶️ Ejecución

```bash
python main.py
```

---

### 🗂️ Estructura del Proyecto

```text
/dao       → Lógica de acceso a datos con patrón DAO  
/models    → Clases del modelo de datos  
/views     → Lógica de la interfaz de consola  
/utils     → Funciones utilitarias y conexión a la DB  
main.py    → Archivo principal para ejecutar la app  
```


