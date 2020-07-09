#!/usr/bin/python3
''' itsOrD || populating sqlite db for practice '''


import sqlite3
conn = sqlite3.connect('test.db')
print('Opened db successfuly')


conn.execute('''
        INSERT INTO COMPANY (ID, NAME, AGE, ADDRESS, SALARY)
        VALUES (1, 'Pup', 36, '123 Internet way', 20000.00)
        ''')

conn.execute('''
        INSERT INTO COMPANY (ID, NAME, AGE, ADDRESS, SALARY)
        VALUES (2, 'Broseph', 3, '321 Internet way', 20.00)
        ''')

conn.execute('''
        INSERT INTO COMPANY (ID, NAME, AGE, ADDRESS, SALARY)
        VALUES (3, 'Lippo', 6, '2 Internet way', 2.00)
        ''')

conn.execute('''
        INSERT INTO COMPANY (ID, NAME, AGE, ADDRESS, SALARY)
        VALUES (4, 'Garfield', 9, '666 Internet way', 30000.00)
        ''')


conn.commit()
print('Recs created and added successfully my dude.')
conn.close()
