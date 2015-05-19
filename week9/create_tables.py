from settings import db_name, sql_script
import sqlite3

def main():

    conn = sqlite3.connect(db_name)
    with open(sql_script, 'r') as f:
        conn.executescript(f.read())

if __name__ == '__main__':
    main()
