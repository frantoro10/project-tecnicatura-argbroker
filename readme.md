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





