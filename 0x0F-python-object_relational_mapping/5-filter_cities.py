#!/usr/bin/python3
"""
This script takes in the name of a state
as an argument and lists all cities of 
that state, database `hbtn_0e_4_usa`.
"""

import MySQLdb
from sys import argv

if __name__ == '__main__':
    """
    Access to the database and get the states
    from the database.
    """
    db_connect = MySQLdb.connect(
        host="localhost", user=argv[1], port=3306, passwd=argv[2], db=argv[3])

    db_cursor = db_connect.cursor()

    db_cursor.execute("SELECT cities.name FROM cities JOIN states \
            ON cities.state_id = states.id WHERE states.name = %(state_name)s \
            ORDER BY cities.id ASC", {'state_name' : argv[4]})

    rows_selected = db_cursor.fetchall()
    longueur = len(rows_selected)
    if longueur != 0:
        for i in range(longueur - 1):
            print("{}, ".format(rows_selected[i][0]), end="")
        print(rows_selected[longueur - 1][0])
    db_cursor.close()
    db_connect.close()
