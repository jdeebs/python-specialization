# Import the necessary SQLAlchemy modules and classes

# Core functionality for defining tables and creating the database engine
from sqlalchemy import create_engine, Column
# Data types for table columns
from sqlalchemy.types import Integer, String
# ORM tools for managing sessions and defining models
from sqlalchemy.orm import sessionmaker, declarative_base

# Create database engine to establish connection with existing
# MySQL database using MySQL credentials
engine = create_engine("mysql://cf-python:password@localhost/task_database")

# Create a session factory that binds sessions to the engine
## Manages connections to the database via the engine
Session = sessionmaker(bind=engine)
# Create a session instance to interact with database
## Active connection to the database
session = Session()

# Create a declarative base class to define ORM models
## Binds the python class to database tables
Base = declarative_base()
# Define Recipe class
## Inherits from Base making it part of the declarative system
## Needed so that the ORM can translate python -> MySQL
class Recipe(Base):
    # Define 'final_recipes' table
    __tablename__ = "final_recipes"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50))
    ingredients = Column(String(255))
    cooking_time = Column(Integer)
    difficulty = Column(String(20))

    # Method to show a quick string representation of the recipe
    def __repr__(self):
        return "<Recipe ID: " + str(self.id) + "-" + self.name + ">"
    
    # Method to print a formatted string representation of the recipe
    def __str__(self):
        # Format ingredients list
        ingredients_formatted = ", ".join(self.ingredients.split(', '))

        recipe_details = (
            f"Recipe: {self.name}\n"
            f"Cooking Time (min): {self.cooking_time}\n"
            f"Ingredients: {ingredients_formatted}\n"
            f"Difficulty level: {self.difficulty}"
            )
        # Calculate dynamic line width
        line_width = max(len(line) for line in recipe_details.split("\n"))
        dashed_line = "-"*line_width
        
        # Combine details with dynamic lines
        return f"\n{dashed_line}\n{recipe_details}\n{dashed_line}\n"
    
    # Method to calculate difficulty of a recipe based on number of ingredients and cooking time
    def calculate_difficulty(self, cooking_time, ingredients):
        if cooking_time < 10 and len(ingredients) < 4:
            difficulty = "Easy"
        elif cooking_time < 10 and len(ingredients) >= 4:
            difficulty = "Medium"
        elif cooking_time >= 10 and len(ingredients) < 4:
            difficulty = "Intermediate"
        elif cooking_time >= 10 and len(ingredients) >= 4:
            difficulty = "Hard"
        else:
            difficulty = None

        # Update difficulty based on above conditions
        self.difficulty = difficulty

    # Method to retrieve ingredients string as a list
    def return_ingredients_as_list(self, ingredients):
        if self.ingredients == '':
            return []
        else:
            ingredient_list = self.ingredients.split(", ")
            return ingredient_list

# Base tracks all ORM models, metadata stores tables/columns
# info, create_all sends SQL commands to create the
# tables/columns in the database, requires 'engine' argument
# to connect to the database
Base.metadata.create_all(engine)