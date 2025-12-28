# Database Project

This project is a **database management system application** developed in **Python**.
The main goal of the project is to demonstrate correct work with a **relational database (MySQL)** and the use of the **Repository pattern (D1)**.

The application supports CRUD operations, transactions across multiple tables, data import, reporting using database views and configuration via an external file.

---

## Project Structure

```
DATABASE/
├── config/
│   └── config.yaml
├── db/
│   ├── init_db.sql
│   └── seed_data.sql
├── imports/
│   ├── import_csv.py
│   ├── import_json.py
│   └── import_xml.py
├── models/
│   ├── zakaznik.py
│   ├── produkt.py
│   ├── objednavka.py
│   └── polozka.py
├── repositories/
│   ├── base_repository.py
│   ├── zakaznik_repository.py
│   ├── produkt_repository.py
│   ├── sklad_repository.py
│   ├── objednavka_repository.py
│   └── polozka_repository.py
├── services/
│   ├── objednavka_service.py
│   └── report_service.py
├── main.py
├── requirements.txt
└── README.md
```

---

## Application Overview

The application manages:
- Customers
- Products
- Stock
- Orders

Orders are created across multiple tables and processed using a **database transaction**.
If any part of the transaction fails, all changes are rolled back.

Reports are generated using **database views** and contain aggregated data from multiple tables.

---

## Installation and Setup

### Prerequisites

- Python **3.10 or newer**
- **MySQL Server** (8.0 recommended)
- MySQL client (CLI or MySQL Workbench)
- pip

---

## 1. Database Setup

### 1.1 Create Database

```sql
CREATE DATABASE projekt_d1_db;
```

### 1.2 Create Database Structure

Execute the SQL script:

```
db/init_db.sql
```

This script creates:
- Tables
- Relationships (including M:N)
- Views

Verify creation:

```sql
SHOW TABLES;
SHOW VIEWS;
```

---

## 2. Database Configuration

Edit the configuration file:

```
config/config.yaml
```

Example configuration:

```yaml
database:
  host: localhost
  user: root
  password: password
  name: projekt_d1_db
```

Make sure the credentials match your MySQL setup.

---

## 3. Install Dependencies

From the project root directory:

```bash
python -m pip install -r requirements.txt
```

Verify installation:

```bash
python -c "import mysql.connector; print('OK')"
```

---

## 4. Run the Application

Run the application from the project root directory: 

```bash
python main.py
```

The application is executable **without an IDE**, as required by the assignment.

---

## 5. Data Import

The application supports importing data into multiple tables from:
- CSV
- JSON
- XML

Import scripts are located in:

```
imports/
```

---

## 6. Reports

Reports are generated using **database views** and include:
- Aggregated data
- Data from multiple related tables
- Counts, sums, minimums and maximums

---

## Testing

Testing is performed using **manual test scenarios**.

Test documentation:

```
test/TestCases.pdf
```

The application is tested by a third-party tester according to the provided scenarios.

---

## Notes

- The MySQL server must be running before starting the application
- The project follows the **Repository pattern (D1)**
- SQLite is not used
- The project is suitable for submission as a **D1 portfolio project**

---

## Assignment Compliance

✔ Relational database (MySQL)  
✔ Repository pattern (D1)  
✔ Minimum 5 tables and M:N relationship  
✔ CRUD operations across multiple tables  
✔ Transactions  
✔ Database views and reports  
✔ Data import  
✔ Configuration file  
✔ Error handling  
✔ Test scenarios

