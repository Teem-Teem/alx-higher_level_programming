#!/usr/bin/python3

import MySQLdb
from sys import argv

"""
This script is safe from MySQL injections!
"""

if __name__ == '__main__':

    db = MySQLdb.connect(host="localhost", user=argv[1], port=3306,
                         passwd=argv[2], db=argv[3])

    with db.cursor() as cur:
        cur.execute("""
             SELECT
                 *
             FROM
                 states
             WHERE
                 name LIKE BINARY %(name)s
             ORDER BY
                 states.id ASC
         """, {
             'name': argv[4]
         })

         rows = cur.fetchall()
    if row is not None:
        for row in rows:
            prit(row)
