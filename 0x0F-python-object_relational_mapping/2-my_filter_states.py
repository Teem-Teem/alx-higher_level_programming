#!/usr/bin/python3


import MySQLdb
from sys import argv

'''
Script that lists all states from the database
'''
if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                           password=argv[2], database=argv[3])
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states WHERE name LIKE"
                   " '{:s}' ORDER BY id ASC".format(argv[4]))
    rows = cursor.fetchall()
    
    for row in rows:
        print(row)
