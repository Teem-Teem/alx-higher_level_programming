#!/usr/bin/python3
""" List all state in database """


from sys import argv
import MySQLdb

if __name__ == '__main__':

    db_user = argv[1]
    db_passwd = argv[2]
    db_name = argv[3]

    database = MySQLdb.connect(host='localhost',
                               port=3306,
                               user=argv[1],
                               passwd=argv[2],
                               db=argv[3])

    cursor = database.cursor()

    cursor.execute('SELECT id, name FROM states ORDER BY states.id ASC')

    for row in cursor.fetchall():
        print(row)

