from settings import db_name, API_link
import requests
import sqlite3

class LastHR:

    def __init__(self):
        self.db = sqlite3.connect(db_name)
        self.db.row_factory = sqlite3.Row
        self.cursor = self.db.cursor()
        self.link = LastHR.get_API(API_link)

    @staticmethod
    def get_API(link):
        API_info = requests.get(link)
        return API_info.json()

    def populate_students_table(self):
        for structure in self.link:
            self.cursor.execute('''INSERT INTO Students(student_name, GitHub_account) VALUES (?,?)''',(structure['name'], structure['github']))
        self.db.commit()

    def populate_courses_table(self):
        course_set = set()
        for structure in self.link:
            for course in structure['courses']:
                course_set.add(course['name'])
        for course in course_set:
            self.cursor.execute('''INSERT INTO Courses(course_name) VALUES (?)''', (course,))
        self.db.commit()

    def connection_students_courses(self):
        st_co = set()
        for students in self.link:
            if students['courses'] is not ['']:
                for course in students['courses']:
                    self.cursor.execute('''SELECT e1.id, e2.id FROM Students AS e1, Courses AS e2
                        WHERE e1.student_name = ? AND e2.course_name = ?''', (students['name'], course['name']))
                    for row in self.cursor:
                        st_co.add(row)
        return st_co

    def populate_junction_table(self):
        relation = self.connection_students_courses()
        for r in relation:
            self.cursor.execute('''INSERT INTO Students_to_Courses(students_id, courses_id) VALUES (?,?)''', (r[0], r[1]))
        self.db.commit()

    def list_students(self):
        self.cursor.execute('''SELECT student_name, GitHub_account FROM Students''')
        for row in self.cursor:
            print('Student name: {}, GitHub account: {}'.format(row['student_name'], row['GitHub_account']))

    def list_courses(self):
        self.cursor.execute('''SELECT * FROM Courses''')
        for row in self.cursor:
            print('{} {}'.format(row['id'], row['course_name']))

    def list_students_to_courses(self):
        self.cursor.execute('''SELECT e1.student_name, e2.course_name
                            FROM Students AS e1, Courses AS e2, Students_to_Courses as e3
                            WHERE e1.id = e3.students_id AND e2.id = e3.courses_id''')
        for row in self.cursor:
            print('Student: {}, Course: {}'.format(row['student_name'], row['course_name']))

    def list_student_with_most_courses(self):
        self.cursor.execute('''SELECT e1.student_name, COUNT(e2.students_id) FROM Students AS e1, Students_to_Courses as e2
                            WHERE e1.id = e2.students_id GROUP BY students_id
                            ORDER BY COUNT(students_id) DESC LIMIT 10''')
        print('TOP 10 students with most attended courses:')
        for row in self.cursor:
            print('{} - {}'.format(row['student_name'], row['COUNT(e2.students_id)']))



def main():
    TLHR = LastHR()
    #TLHR.populate_students_table()
    #TLHR.populate_courses_table()
    #TLHR.populate_junction_table()
    TLHR.list_students()
    TLHR.list_courses()
    TLHR.list_students_to_courses()
    TLHR.list_student_with_most_courses()

if __name__ == '__main__':
    main()
