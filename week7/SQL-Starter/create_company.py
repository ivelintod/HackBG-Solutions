import sqlite3


class CreateTable:

    def __init__(self, database):
        self.database = database
        self.db = sqlite3.connect(database)
        self.cursor = self.db.cursor()
        self.create_table_query = '''
                        CREATE TABLE employees(id INTEGER PRIMARY KEY, name TEXT,
                       monthly_salary TEXT, yearly_bonus TEXT, position TEXT)'''
        self.result = None

    def open_database(self):
        self.db = sqlite3.connect(self.database)
        self.cursor = self.db.cursor()

    def create_table(self):
        try:
            self.cursor.execute(self.create_table_query)
            self.db.commit()
        except sqlite3.OperationalError:
            self.db.rollback()
            print("Table employees already exists!")
        finally:
            self.db.close()

    def insert_values(self, i, name, monthly_salary, yearly_bonus, position):
        self.open_database()
        try:
            self.cursor.execute('''INSERT INTO employees(id, name, monthly_salary, yearly_bonus, position)
            VALUES (?, ?, ?, ?, ?)''', (i, name, monthly_salary, yearly_bonus, position))
            self.db.commit()
        except sqlite3.IntegrityError:
            print("Record already exists!")
        finally:
            self.db.close()

    def delete_values(self, i):
        self.open_database()
        try:
            self.cursor.execute('''DELETE FROM employees WHERE id = ? ''', (i,))
            self.db.commit()
        except sqlite3.IntegrityError:
            print("No such record found!")
        finally:
            self.db.close()

    def update_values(self, i):
        self.open_database()
        name = input("name>")
        monthly_salary = input("monthly_salary>")
        yearly_bonus = input("yearly_bonus>")
        position = input("position>")
        try:
            self.cursor.execute('''UPDATE employees SET name = ? WHERE id = ?''',(name, i))
            self.cursor.execute('''UPDATE employees SET monthly_salary = ? WHERE id = ?''',(monthly_salary, i))
            self.cursor.execute('''UPDATE employees SET yearly_bonus = ? WHERE id = ?''',(yearly_bonus, i))
            self.cursor.execute('''UPDATE employees SET position = ? WHERE id = ?''',(position, i))
            self.db.commit()
        except sqlite3.IntegrityError:
            print("No such id!")

    def table_view(self):
        self.open_database()
        self.result = self.cursor.execute("SELECT * FROM employees")
        #for row in self.result:
        #    print(row)

s = CreateTable('Hack_employees.db')
#s.create_table()
#s.insert_values(1, "Ivan Ivanov", 5000, 10000, "Software Develo7er")
#s.insert_values(2, "Rado Rado", 500, 0, "Technical Support Intern")
#s.insert_values(3, "Ivo Ivo", 10000, 100000, "CEO")
#s.insert_values(4, "Petar Petrov", 3000, 1000, "Marketing Manager")
#s.insert_values(5, "Maria Georgieva", 8000, 10000, "COO")'''
#s.delete_values(10000)
#s.list_employees()

