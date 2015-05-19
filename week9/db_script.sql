DROP TABLE IF EXISTS clients;
CREATE TABLE clients(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT,
            password TEXT,
            balance REAL DEFAULT 0,
            message TEXT,
            email TEXT);

DROP TABLE IF EXISTS login_track;
CREATE TABLE login_track(
            client_id INTEGER,
            login_attempt INTEGER DEFAULT 0,
            time REAL DEFAULT 0,
            FOREIGN KEY (client_id) REFERENCES clients(id));

