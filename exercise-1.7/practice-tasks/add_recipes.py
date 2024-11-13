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
