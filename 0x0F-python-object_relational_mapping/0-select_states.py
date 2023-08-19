#!/usr/bin/python3
"""
List all state in the database 'hbtn_0e_0_usa'.
"""

from sys import argv
import MySQLdb

if __name__ == '__main__':

    db_username = argv[1]
    db_password = argv[2]
    db_name = argv[3]

    db = MySQLdb.connect(host="localhost", port=3306, username=arg[1], password=argv[2], db=argv                         [3])

    cursor = databse.cursor()

    cursor.execute("SELECT * FROM states")
    row = cursor.fetchall()

    for row in rows:
        print(row)

