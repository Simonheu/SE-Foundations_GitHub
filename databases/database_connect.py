## simple demo script for showing how to connect to an sqlite DB 
# from Python, and run a simple SQL query 

# import the python library for SQLite // allows us to handle databases
import sqlite3

# connect to the database file, and create a connection object // opens the connection 
db_connection = sqlite3.connect('restaurants.db')

# create a database cursor object, which allows us to perform SQL on the database. //cursor: tells you where you are in the database
db_cursor = db_connection.cursor()

# run a first query 
#db_cursor.execute("SELECT * from restaurants") #give me all the colums from "restaurant table" //gets all the informaton
#db_cursor.execute("SELECT NAME FROM restaurants")
db_cursor.execute("""SELECT restaurants.NAME, neighborhoods.NAME 
                        FROM neighborhoods 
                        INNER JOIN restaurants 
                        ON neighborhoods.ID=restaurants.NEIGHBORHOOD_ID
                        WHERE neighborhoods.NAME='Kreuzberg'""")

# store the result in a local variable. 
# this will be a list of tuples, where each tuple represents a row in the table
list_restaurants = db_cursor.fetchall() #//fetchal creates a more "readable" format and stores it in the variable

print("list_restaurants contents:")
print(list_restaurants) #//returns a list of tuples. >>why tuples? >>its immutable

db_connection.close()


