# Import MySQL python connector
import mysql.connector

# Init connection object
# Connects with MySQL host, user, and passwd params
# that were setup when MySQL database was installed
conn = mysql.connector.connect(
    host='localhost',
    user='cf-python',
    passwd='password')

# Init cursor object from MySQL connection
cursor = conn.cursor()

# Create database and check that it doesn't exist
cursor.execute("CREATE DATABASE IF NOT EXISTS task_database")

# Access database with script
cursor.execute("USE task_database")

# Create a table called Recipes with columns
# id, name, ingredients, cooking_time, difficulty
cursor.execute('''CREATE TABLE IF NOT EXISTS Recipes
               id INT,
               name VARCHAR(50),
               ingredients VARCHAR(255),
               cooking_time INT,
               difficulty VARCHAR(20)
               ''')