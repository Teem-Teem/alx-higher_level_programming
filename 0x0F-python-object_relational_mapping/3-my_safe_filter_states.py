#!/usr/bin/python3

import MySQLdb
from sys import argv

"""
This script is safe from MySQL injections!
"""

if __name__ == '__main__':

    db_user = argv[1]
    db_passwd = argv[2]
    db_name = argv[3]
    search = '{}'.format(argv[4])

    db = MySQLdb.connect(host="localhost", port=3306, user=db_user,
                         passwd=db_passwd, db=argv[3])

    cur = db.cursor()

    cur.execute("SELECT id, name FROM states\
                WHERE name = %s\
                ORDER BY states.id ASC;", (search,))
    {
    "name" : argv[4]
    })


    rows = cur.fetchall()

    for row in rows:
        print(row)