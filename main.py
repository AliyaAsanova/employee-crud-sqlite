# -*- coding: utf-8 -*-

from employee import Employee
from employee_dao import EmployeeDAO

def main():
    dao = EmployeeDAO()
    dao.create_table()  # создаём таблицу, если её нет

    print("=== INSERT ===")
    emp1 = Employee(None, "Aliia", "Data Analyst", 70000.0, "2025-04-06")
    dao.insert(emp1)

    print("=== GET ALL ===")
    all_emps = dao.get_all()
    for emp in all_emps:
        print(emp)

    print("=== GET BY ID ===")
    emp = dao.get_by_id(1)
    if emp:
        print(emp)

    print("=== UPDATE ===")
    if emp:
        emp.salary = 75000.0
        emp.position = "Senior Analyst"
        dao.update(emp)

    print("=== AFTER UPDATE ===")
    emp = dao.get_by_id(1)
    print(emp)

    print("=== DELETE ===")
    dao.delete(1)

    print("=== AFTER DELETE ===")
    all_emps = dao.get_all()
    for emp in all_emps:
        print(emp)

    dao.close()

if __name__ == "__main__":
    main()

