# Import the necessary SQLAlchemy modules and classes

# Core functionality for defining tables and creating the database engine
from sqlalchemy import create_engine, Column
# Data types for table columns
from sqlalchemy.types import Integer, String
# ORM tools for managing sessions and defining models
from sqlalchemy.orm import sessionmaker, declarative_base

# Create a database engine that establishes a connection to the existing MySQL database
# "cf-python" is the username, "password" is the password, "localhost" is the host, and "my_database" is the database name
engine = create_engine("mysql://cf-python:password@localhost/my_database")

# Create a session factory that binds sessions to the engine
Session = sessionmaker(bind=engine)
# Create a session instance from the session factory to interact with the database
session = Session()
# Create a declarative base class for defining ORM models
Base = declarative_base()


# Define the ORM model for the "practice_recipes" table
class Recipe(Base):
    __tablename__ = "practice_recipes"

    # Define the columns in the table
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50))
    ingredients = Column(String(255))
    cooking_time = Column(Integer)
    difficulty = Column(String(20))

    # Define how instances of this class are represented as strings
    def __repr__(self):
        return "<Recipe ID: " + str(self.id) + "-" + self.name + ">"

# Create a list of Recipes with predefined values to use as sample data
recipes = [
    Recipe(name="Tea", cooking_time=5, ingredients="Tea Leaves, Water, Sugar", difficulty="Easy"),
    Recipe(name="Pasta", cooking_time=20, ingredients="Pasta, Tomato Sauce, Olive Oil", difficulty="Medium"),
    Recipe(name="Omelette", cooking_time=10, ingredients="Eggs, Salt, Pepper", difficulty="Easy"),
    Recipe(name="Salad", cooking_time=15, ingredients="Lettuce, Tomato, Cucumber, Dressing", difficulty="Easy")
]

# Add all the Recipe instances to the session at once
session.add_all(recipes)
# Commit the session to save the new recipes to the database
session.commit()

# Assign recipes from database to a variable to be accessible using dot notation
recipes_list = session.query(Recipe).all()

# Examples to query individually
recipes_list[0].id
recipes_list[0].name
recipes_list[3].name
recipes_list[0].ingredients
recipes_list[0].cooking_time

# Example to query all recipe details formatted, using a for loop
for recipe in recipes_list:
    print("Recipe ID: ", recipe.id)
    print("Recipe Name: ", recipe.name)
    print("Ingredients: ", recipe.ingredients)
    print("Cooking Time: ", recipe.cooking_time)

######################################################
######## QUERY METHODS ###############################

# Retrieve a single object using get() method
# get() uses primary key to specify which row
session.query(Recipe).get(1)

# Retrieve one or more objects using filter() method
# requires a "final method" to get the resultant object
# otherwise returns a query object
# final method in this case is .one()
'''
all() - returns a list of all objects from the query (output type: list)
one() - returns only one object, if only one object is resultant from your query (output type: object from your table)
first() - returns the first object from a list of results (output type: object from your table)
get(id) - returns an object with an id that matches with the primary key (output type: object from your table)
'''
session.query(Recipe).filter(Recipe.name == 'Coffee').one()

# Retrieve objects using bits of strings or patterns in row values with like() method
# uses the % wildcard on either side to check if
# entries contain "Water" rather than exactly matches
# 'Water'
session.query(Recipe).filter(Recipe.ingredients.like("%Water%")).all()

# Can also search for multiple conditions separating
# them with commas in the argument
# Searches for both 'Milk' and 'Baking Powder'
session.query(Recipe).filter(Recipe.ingredients.like("%Milk%"), Recipe.ingredients.like("%Baking Powder%")).all()

# For any arbitrary number of conditions
# append each condition to a list and use a preceding
# asterisk '*' within the filter method
condition_list = [
    Recipe.ingredients.like("%Milk%"),
    Recipe.ingredients.like("%Baking Powder%")
]
session.query(Recipe).filter(*condition_list).all()

# Make direct changes using the update() method
# expects a dictionary as its argument, must have
# dictionary syntax -> { }
# Rename Cake recipe to Birthday Cake
session.query(Recipe).filter(Recipe.name == 'Cake').update({Recipe.name: 'Birthday Cake'})