#!/usr/bin/python3
""" Returns all cities of user inputted state """
import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])
    cur = db.cursor()
    cur.execute(
        "SELECT cities.id, cities.name, states.name FROM cities \
        LEFT JOIN states ON cities.state_id = states.id WHERE \
        states.name = \"{}\"".format(argv[4]))
    cities = cur.fetchall()
    cities = [city[1] for city in cities]
    print(", ".join(cities))
    cur.close()
    db.close()
