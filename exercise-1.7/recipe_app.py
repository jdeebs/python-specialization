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

################ FUNCTIONS ################

def create_recipe():
    print("Enter your recipe info!\n")
    
    # Get user input for name and cooking time
    while True:
        try:
            name = input("Recipe name: ").strip().title()
            if len(name) <= 50:
                break
            elif len(name) > 50:
                print("Recipe name must be less than 50 characters.")
                continue
            else:
                print("Recipe name cannot be empty. Please enter a valid name.")
        except ValueError:
            print("Invalid name. Please enter a valid name for your recipe.")
    while True:
        try:
            cooking_time = int(input("Cooking time (in minutes): "))
            if cooking_time > 0:
                break
            # Handle empty input
            elif not cooking_time:
                print("Cooking time cannot be empty. Please enter a valid cooking time.")
            else:
                print("Cooking time must be a positive number.")
        except ValueError:
            print("Invalid cooking time. Please enter a number for cooking time.")

    # Get ingredients as a list
    ingredients = []
    print("Enter ingredients one by one (type 'done' to finish):")
    # Append each ingredient until user types done
    while True:
        try:
            ingredient = str(input("Ingredient: ")).strip()
            if ingredient.lower() == 'done':
                break
            # Handle empty input
            elif not ingredient:
                print("Ingredient cannot be empty. Please enter a valid ingredient.")
                continue
            ingredients.append(ingredient.capitalize())
        except ValueError:
            print("Invalid ingredient. Please enter a valid ingredient for your recipe.")

    # Convert ingredients list to comma separated string
    ingredients_str = ", ".join(ingredients)

    # Create recipe instance and calculate difficulty
    recipe_entry = Recipe(
    name=name, 
    cooking_time=cooking_time, ingredients=ingredients_str, 
    difficulty=None)

    recipe_entry.calculate_difficulty(cooking_time, ingredients)

    # Add recipe to database
    session.add(recipe_entry)
    session.commit()
    print("Recipe created successfully!")
    return recipe_entry

def view_all_recipes():
    # Retrieve all recipes from the database as a list
    recipes_list = session.query(Recipe).all()

    # Handle if list is empty
    if not recipes_list:
        print("There aren't any existing recipes.")
        return None
    
    # Loop through recipes and call their respective __str__ methods to display each recipe
    for recipe in recipes_list:
        recipe.__str__()

