#!/usr/bin/python3
''' itsOrD || picking out specific data from db '''


import sqlite3


conn = sqlite3.connect('test.db')
print('Opened database successfully')

conn.execute('UPDATE COMPANY set SALARY = 25000.00 where ID = 1')
conn.commit()
print('Total number of rows updated : ', conn.total_changes)

cursor = conn.execute('SELECT id, name, address, salary from COMPANY')
for row in cursor:
    print('ID = ', row[0])
    print('Name = ', row[1])
    print('Address = ', row[2])
    print('Salary = ', row[3], "\n")

print('Operation done boiiii')
conn.close()
