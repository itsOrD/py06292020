#!/usr/bin/python3

import sqlite3

conn = sqlite3.connect('test.db')

print('Opened db successfully')
conn.execute(f'''
        CREATE TABLE IF NOT EXISTS COMPANY
        (
            ID          INT     NOT NULL    PRIMARY KEY,
            NAME        TEXT    NOT NULL,
            AGE         INT,
            ADDRESS     CHAR(50),
            SALARY      REAL
        );
    ''')
print('Table created successfully')
conn.close()
