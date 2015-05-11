import sqlite3
import sys

def main():

    SQL_script = sys.argv[1]
    db_name = sys.argv[2]

    db = sqlite3.connect(db_name)
    cursor = db.cursor()

    with open(SQL_script, 'r') as script:
        cursor.executescript(script.read())
        db.commit()

if __name__ == '__main__':
    main()
