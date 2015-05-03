import sqlite3
from create_company import CreateTable


class CompanyManager:

    def __init__(self, database):
        self.company = CreateTable(database)
        self.company.create_table()
        self.index = 0
        self.company.table_view()
        for row in self.company.result:
            self.index += 1

    def list_employees(self):
        self.company.table_view()
        for row in self.company.result:
            print("{} - {} - {}".format(row[0], row[1], row[4]))

    def monthly_spending(self):
        self.company.table_view()
        monthly_expense = 0
        for row in self.company.result:
            monthly_expense += int(row[2])
        print("The company is spending ${} every month!".format(monthly_expense))

    def yearly_spending(self):
        self.company.table_view()
        yearly_expense = 0
        for row in self.company.result:
            yearly_expense += 12 * int(row[2]) + int(row[3])
        print("The company is spending ${} every year!".format(yearly_expense))

    def add_employee(self):
        name = input("name>")
        monthly_salary = input("monthly_salary>")
        yearly_bonus = input("yearly_bonus>")
        position = input("position>")
        self.index += 1
        self.company.insert_values(self.index, name, monthly_salary, yearly_bonus, position)

    def delete_employee(self, n):
        self.company.delete_values(n)

    def update_employee(self, n):
        self.company.update_values(n)




#company1 = CompanyManager()
#company1.list_employees()
#company1.monthly_spending()
#company1.yearly_spending()
#company1.add_employee()
#company1.delete_employee(6)
#company1.delete_employee(7)
#company1.update_employee(2)
#company1.list_employees()
