import sqlite3
from create_company import CreateTable
from manage_company import CompanyManager
import sys

def main():
    command = input("Create database name(respecively - file): ")
    manager = CompanyManager(command + '.db')
    #manager.company.create_table()

    while True:
        command = input("command>")
        if command == 'add_employee':
            manager.add_employee()
        if command == 'list_employees':
            manager.list_employees()
        if command == 'monthly_spending':
            manager.monthly_spending()
        if command == 'yearly_spending':
            manager.yearly_spending()
        if command == 'delete_employee':
            id_prompt = input('')
            manager.delete_employee(id_prompt)
        if command == 'update_employee':
            id_prompt = input('')
            manager.update_employee(id_prompt)
        if command == 'exit':
            sys.exit()

if __name__ == "__main__":
    main()
