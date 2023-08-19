#!/usr/bin/python3
"""
List all state in the database 'hbtn_0e_0_usa'.
"""

import MySQLdb
from sys import argv

if __name__ == '__main__':

    db_username = argv[1]
    db_password = argv[2]
    db_name = argv[3]

    db = MySQLdb.connect(host="localhost", username=arg[1], port=3306,
                         password=argv[2], db=argv[3])


    cursor = databse.cursor()

    cursor.execute("SELECT * FROM states")
    row = cursor.fetchall()

    for row in rows:
        print(row)

