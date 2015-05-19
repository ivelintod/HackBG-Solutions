from settings_for_tests import DB_NAME, DB_SCRIPT
import sqlite3


def main():
    db = sqlite3.connect(DB_NAME)
    with open('../' + DB_SCRIPT, 'r') as f:
        db.executescript(f.read())
    db.commit()

if __name__ == '__main__':
    main()
