# Employee CRUD Management System (SQLite + Python)

## Objective

Create a Python application that interacts with a relational database to manage employee data.  
Implements CRUD (Create, Read, Update, Delete) operations for an `employee` table using SQLite.  
Includes:
- `Employee` class (data entity)
- `EmployeeDAO` class (database access)

---

## Project Structure

. ├── employee.py # Employee class with attributes and str method ├── employee_dao.py # DAO class with all CRUD operations ├── main.py # Script to test the database functionality ├── employee_db.sqlite # SQLite database file ├── screenshots/ # Folder with screenshots (DB structure, data, output) └── README.md # Project documentation


---

## Features

- Create a new employee  
- Read employee data by ID  
- Read all employees  
- Update employee records  
- Delete employee by ID  

---

## How to Run

1. Clone the repository:

git clone https://github.com/AliyaAsanova/employee-crud-sqlite.git cd employee-crud-sqlite


2. Run the script:

python main.py
тировать

The program will:
- Create the table if it doesn't exist  
- Insert a new employee  
- Retrieve all employees  
- Retrieve one employee by ID  
- Update employee data  
- Delete an employee  
- Show outputs in the console

---

## 📸 Screenshots

### 🧱 Table Structure (DBeaver)  
![table_structure](https://github.com/user-attachments/assets/7817e2f3-03c7-4c52-bfd9-2b437237b3aa)


### 📊 Data Preview (DBeaver)  
![data_preview](https://github.com/user-attachments/assets/612674bb-a4fd-4653-b4cc-f2671397f8fb)


### 💬 Console Output  
![main_screenshot](https://github.com/user-attachments/assets/2c349973-bdee-41f9-b272-4fd4f4b0e568)


---

## 💻 Sample Console Output

=== INSERT === === GET ALL === ID: 1, Name: Aliia, Position: Data Analyst, Salary: 70000.0, Hire Date: 2025-04-06

=== GET BY ID === ID: 1, Name: Aliia, Position: Data Analyst, Salary: 70000.0, Hire Date: 2025-04-06

=== UPDATE === === AFTER UPDATE === ID: 1, Name: Aliia, Position: Senior Analyst, Salary: 75000.0, Hire Date: 2025-04-06

=== DELETE === === AFTER DELETE ===

---
