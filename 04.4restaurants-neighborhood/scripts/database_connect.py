#!/usr/local/bin/python3

## simple demo script for showing how to connect to an sqlite DB 
# from Python, and run a simple SQL query 

import cgi

# import the python library for SQLite 
import sqlite3

def get_restaurants(neighborhood_input):	
	# connect to the database file, and create a connection object
	db_connection = sqlite3.connect('scripts/restaurants.db')

	# create a database cursor object, which allows us to perform SQL on the database. 
	db_cursor = db_connection.cursor()

	# run a first query 
    # define a query, taking the string input for the neighborhood name 

    list_restaurants = """SELECT * from restaurants
                INNER JOIN neighborhoods ON restaurants.NEIGHBORHOOD_ID=neighborhoods.ID
                WHERE neighborhoods.NAME="{neighborhood_placeholder}"
            """.format(neighborhood_placeholder=neighborhood_input)
	
	db_cursor.execute(list_restaurants)

# get the output of the form.
form = cgi.FieldStorage()

# get an input filed from the form called 'name'
# and assign it's value to a local variable called v_name
n_name = form.getvalue('name')

get_restaurants(n_name)

list_restaurants = db_cursor.fetchall()

def smth(list_restaurants):
	for l in list_restaurants:
		print("""
			<html>
			<body>
			<p><strong>
				- {} : 
			</strong></p>
			</body>
			</html>
			""".format(l))
smth(list_restaurants)

db_connection.close()
