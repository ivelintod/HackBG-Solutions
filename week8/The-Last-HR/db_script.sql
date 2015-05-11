DROP TABLE IF EXISTS Students;
CREATE TABLE Students(id INTEGER PRIMARY KEY AUTOINCREMENT,
                      student_name TEXT, GitHub_account TEXT);

DROP TABLE IF EXISTS Courses;
CREATE TABLE Courses(id INTEGER PRIMARY KEY AUTOINCREMENT,
                     course_name TEXT);

DROP TABLE IF EXISTS Students_to_Courses;
CREATE TABLE Students_to_Courses(students_id INTEGER, courses_id INTEGER,
                                FOREIGN KEY(students_id) REFERENCES Students(id),
                                FOREIGN KEY(courses_id) REFERENCES Courses(id));

