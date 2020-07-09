#!/usr/bin/python3
''' itsOrD || deleting data from db '''


import sqlite3


conn = sqlite3.connect('test.db')
print('Opened database successfully')

conn.execute('DELETE from COMPANY where id = 2;')
conn.commit()
print('Total number of rows deleted : ', conn.total_changes)

cursor = conn.execute('SELECT id, name, address, salary from COMPANY')
for row in cursor:
    print('Id = ', row[0])
    print('Name = ', row[1])
    print('Address = ', row[2])
    print('Salary = ', row[3], '\n')

print('Op complete.')
conn.close()
