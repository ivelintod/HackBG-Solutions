from settings import db_name
from settings import sql_script
import sqlite3

def main():

    conn = sqlite3.connect(db_name)

    with open(sql_script, 'r') as f:
        conn.executescript(f.read())

    conn.commit()

if __name__ == '__main__':
    main()
