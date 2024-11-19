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
        return "<ID: " + str(self.id) + ", Name: " + self.name + ">"
    
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
        # Fixed line width
        fixed_width = 50
        dashed_line = "-" * fixed_width
        
        # Combine details with dynamic lines
        return f"\n{dashed_line}\n{recipe_details}\n{dashed_line}"
    
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
            if len(name) <= 50 and len(name) > 0:
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
        print(recipe)

def search_by_ingredients():
    # Use count() to check number of entries (rows) in the table and handle if the there are no entries
    if not session.query(Recipe).count():
        print("There aren't any existing recipes to pull ingredients from.")
        return None
    
    # Store ingredients in results variable
    results = session.query(Recipe.ingredients).all()
    
    # Use a set to handle duplicates
    all_ingredients = set()
    # Iterate through each row entry and split ingredients to append them to the all_ingredients list
    for row in results:
        # Need index number to loop through tuples
        if row[0]:
            # Split the string by space to get individual ingredients
            ingredient = row[0].split(", ")
            # Add each ingredient to the set, ignoring duplicates
            all_ingredients.update(ingredient)
        
    # Convert all_ingredients from set to list so it can be indexed
    all_ingredients = list(all_ingredients)

    # Display ingredients
    print("\nAll recipe ingredients:\n")

    # Display all ingredients with indexes
    # Parse through ingredients list and enumerate each ingredient, printing the index associated
    for index, ingredient in enumerate(all_ingredients):
        print(f"{index}: {ingredient}")
    
    while True:
        # Ask user for which ingredients to search and find matching recipes
        user_input = input("\nEnter the indexes of ingredients you wish to see recipes for, separated by spaces. Type 'quit' to exit.\n(Example: 1 5 13): ")
        # Handle quit
        if user_input == 'quit':
            return
        # Handle non-numeric input
        elif not all(part.isnumeric() for part in user_input.split()):
            print("Indexes must be numeric. Please try again.")
            continue

        # Create a list of user input indexes
        ingredient_indexes = user_input.split(" ")
        # Convert each substring to integer type
        ingredient_indexes = [int(i) for i in ingredient_indexes]

        # Create an available ingredients index
        available_ingredients = []
        invalid_indexes = []

        for i in ingredient_indexes:
            # Check that index is within valid range
            if 0 <= i < len(all_ingredients):
                available_ingredients.append(all_ingredients[i])
            else:
                invalid_indexes.append(i)
            
        # Check if there were any invalid indexes
        if invalid_indexes:
            print("Selected ingredients are not available. Please select from available ingredients.")
            continue
    
        # Check that user input matches available options
        if not invalid_indexes:
            print("You have selected the ingredients:")
        # Loop through selected indexes
            for ingredient in available_ingredients:
                print(ingredient)
            break

    # List containing conditions for every ingredient searched for
    conditions = []

    # Iterate through each searched ingredient and append the search condition to the conditions list
    for ingredient in available_ingredients:
        like_term = f"%{ingredient}%"
        conditions.append(Recipe.ingredients.like(like_term))

    # Retrieve all recipes containing the searched ingredients based on the conditions
    searched_recipes = session.query(Recipe).filter(*conditions).all()

    # Display searched recipes using __str__ method
    for recipe in searched_recipes:
        print(recipe)

def edit_recipe():
    # Check if any recipes exist in the database
    if not session.query(Recipe).count():
        print("There aren't any existing recipes to edit.")
        return None

    # Retrieve ID and name for each recipe from the database and store in 'results' variable
    results = session.query(Recipe.id, Recipe.name).all()

    # Iterate over each item in results and display recipes available to user. Filter ids into list to check later
    recipe_ids = []
    print("Available recipes:")
    for recipe in results:
        recipe_ids.append(recipe[0])
        print(Recipe.__repr__(recipe))

    # User picks recipe by ID
    while True:
        user_input = input("\nEnter the ID of the recipe you want to edit. Type 'quit' to exit: ")
        # Handle quit
        if user_input == 'quit':
            return

        # Convert user input to integer to check ID with correct data type
        try:
            user_input = int(user_input)
            if user_input in recipe_ids:
                break
            # Handle if ID doesn't exist in recipe_ids
            if user_input not in recipe_ids:
                print("The entered ID does not exist. Please try again.")
                continue
        except:
            print("Invalid input. Please enter a valid integer or 'quit'.")
        
    # Retrieve recipe corresponding to ID and store in 'recipe_to_edit' variable
    recipe_to_edit = session.get(Recipe, user_input)

    # Display the recipe details
    print(recipe_to_edit)
    # Prompt user for which to edit
    print("Which column would you like to update?")
    print("1. Name")
    print("2. Cooking Time")
    print("3. Ingredients")
    column_to_update = input("Enter the number for the column to update: ")

    # Edit the selected attribute inside 'recipe_to_edit' object
    column = None
    new_value = None

    # Name attribute
    if column_to_update == "1":
        column = Recipe.name
        new_value = input("Enter the new name for the recipe: ")
        new_value = new_value.title()
        try:
            if new_value.strip() == '':
                print("Name cannot be empty. Returning to main menu.")
                return
            new_value = str(new_value)
            print(f"Recipe name updated to {new_value}.")
            print("\n---------------------------\n")
        except ValueError:
            print("Invalid name. Returning to main menu.")
            return
    # Cooking time attribute
    elif column_to_update == "2":
        column = Recipe.cooking_time
        new_value = input("Enter the new cooking time (in minutes): ")

        try:
            # Convert input to an integer first
            new_value = int(new_value)

            # Check if the cooking time is greater than 0
            if new_value <= 0:
                print("Cooking time must be greater than 0 minutes. Returning to main menu.")
                return
            # If valid
            print(f"Recipe cooking time updated to {new_value} minutes.")
            print("\n---------------------------\n")
        except ValueError:
            print("Invalid cooking time. Please enter a valid integer value for cooking time. Returning to main menu.")
            return
    # Ingredients attribute
    elif column_to_update == "3":
        column = Recipe.ingredients
        ingredients = []
        print("Enter ingredients one by one (type 'done' to finish):")
        try:
            while True:
                ingredient = input("Ingredient: ")
                if ingredient.lower() == 'done':
                    # If ingredients were entered
                    if ingredients:
                        new_value = ", ".join(ingredients)
                        print(f"Ingredients updated to: {new_value}")
                    # If no ingredients were entered
                    else:
                        print("No ingredients entered. Returning to main menu.")
                        return
                    break
                # Check if user entered nothing as ingredient
                elif ingredient.strip() == '':
                    print("Enter a valid ingredient.")
                    continue
                # Update ingredients list
                ingredients.append(ingredient.capitalize())

            # Check if no ingredients were entered
            if not ingredients:
                return
        except ValueError:
            print("Error adding ingredients.")
            print("\n---------------------------\n")
            return
    else:
        print("Invalid choice. Returning to main menu.")
        return

    # Update the selected recipe column
    session.query(Recipe).filter(Recipe.id == user_input).update({column: new_value})
    session.commit()

    # Query the updated recipe
    recipe_to_edit = session.get(Recipe, user_input)
    # Recalculate difficulty using Recipe's class method
    recipe_to_edit.calculate_difficulty(recipe_to_edit.cooking_time, recipe_to_edit.ingredients)

def delete_recipe():
    # Check if any recipes exist in the database
    if not session.query(Recipe).count():
        print("There aren't any existing recipes.")
        return None
    
    # Retrieve ID and name of every recipe and display to user
    results = session.query(Recipe.id, Recipe.name).all()

    recipe_ids = []
    print("Available recipes:")
    for recipe in results:
        recipe_ids.append(recipe[0])
        print(Recipe.__repr__(recipe))

    # Prompt user which recipe to delete by entering corresponding ID
    while True:
        user_input = input("\nEnter the ID of the recipe you want to delete. Type 'quit' to exit: ")
        # Handle quit
        if user_input == 'quit':
            return

        # Convert user input to integer to check ID with correct data type
        try:
            user_input = int(user_input)
            if user_input in recipe_ids:
                break
            # Handle if ID doesn't exist in recipe_ids
            if user_input not in recipe_ids:
                print("The entered ID does not exist. Please try again.")
                continue
        except:
            print("Invalid input. Please enter a valid integer or 'quit'.")
    
    # Retrieve recipe by ID
    recipe_to_delete = session.get(Recipe, user_input)

    # Ask user to confirm choice
    # If user confirms, delete entry from database
    while True:
        confirm_delete = input(f"\nAre you sure you want to DELETE the {recipe_to_delete.name} recipe? Type 'y' to DELETE or 'n' to cancel: ")

        if confirm_delete.lower() == 'n':
            print("Deletion canceled.")
            break
        
        elif confirm_delete.lower() == 'y':
            try:
                session.delete(recipe_to_delete)
                session.commit()
                print("Recipe deleted.")
                return
            except ValueError:
                print("Invalid input. Please enter 'y' or 'n' only.")

def main_menu():
    # Avoid printing the menu multiple times
    # If user chooses an invalid input then set to True
    invalid_input = False
    while True:
        if invalid_input == False:
            print("\nWhat would you like to do?")
            print("1. Create a new recipe")
            print("2. View all recipes")
            print("3. Search for recipes by ingredients")
            print("4. Edit a recipe")
            print("5. Delete a recipe")
            choice = input("\nEnter the number 1-5 or type 'quit' to exit the program: ")
        elif invalid_input == True:
            choice = input("\nEnter the number 1-5 or type 'quit' to exit the program: ")

        if choice == "1":
            create_recipe()
        elif choice == "2":
            view_all_recipes()
        elif choice == "3":
            search_by_ingredients()
        elif choice == "4":
            edit_recipe()
        elif choice == "5":
            delete_recipe()
        elif choice.lower() == "quit":
            print("Exiting the program.")
            # Close session and engine to end program
            session.close()
            engine.dispose()
            break
        else:
            # Set to true to not print entire menu again when user enters invalid input
            invalid_input = True
            print("Invalid input. Please try again.")

main_menu()