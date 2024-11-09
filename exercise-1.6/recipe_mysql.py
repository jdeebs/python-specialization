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
cursor.execute('''CREATE TABLE IF NOT EXISTS Recipes (
               id INT NOT NULL AUTO_INCREMENT,
               name VARCHAR(50),
               ingredients VARCHAR(255),
               cooking_time INT,
               difficulty VARCHAR(20),
               PRIMARY KEY (id)
               )''')

def create_recipe(conn, cursor):
    print("Enter your recipe info")

    # Get user input for name and cooking time

    # Get and validate recipe name
    while True:
        name = input("Recipe name: ").strip().title()
        if name:
            break
        else:
            print("Recipe name cannot be empty. Please enter a valid name.")

    # Get and validate cooking time
    while True:
        try:
            cooking_time = int(input("Cooking time (in minutes): "))
            if cooking_time > 0:
                break
            else:
                print("Cooking time must be a positive integer.")
        except ValueError:
            print("Invalid input. Please enter a number for cooking time.")

    # Get ingredients as a list
    ingredients = []
    print("Enter ingredients one by one (type 'done' to finish): ")
    # Append each ingredient until user types done
    # Capitalize each ingredient
    while True:
        ingredient = str(input("Ingredient: "))
        ingredient = ingredient.capitalize()
        if ingredient.lower() == 'done':
            break
        # Check if user entered nothing as ingredient
        elif ingredient == '':
            print("Enter a valid ingredient.")
            continue
        ingredients.append(ingredient.capitalize())

    # Check if no ingredients were entered
    if not ingredients:
        print("No ingredients entered, recipe was not saved.\nReturning to main menu.")
        print("\n---------------------------\n")
        return
    # Convert ingredients list to a comma separated string
    ingredients_string = ", ".join(ingredients)

    # Store calculated difficulty
    difficulty = calculate_difficulty(cooking_time, ingredients)
    
    # Execute SQL query to insert the recipe
    query = '''INSERT INTO Recipes (name, ingredients, cooking_time, difficulty)
               VALUES (%s, %s, %s, %s)'''
    cursor.execute(query, (name, ingredients_string, cooking_time, difficulty))

    # Commit to save changes
    conn.commit()
    print("Recipe added!")
    print("\n---------------------------\n")
    return

def search_recipe(conn, cursor):
    # Store entire ingredients column w/ tuples on each row containing specific recipe ingredients
    cursor.execute("SELECT ingredients FROM Recipes")
    results = cursor.fetchall()

    # Use a set to handle duplicates
    all_ingredients = set()
    # Iterate over each row in ingredients column
    for row in results:
        # Check for non-empty values
        if row[0]:
            # Split the string by comma and space to get individual ingredients
            ingredients = row[0].split(", ")
            # Add each ingredient to the set, ignoring duplicates
            all_ingredients.update(ingredients)

    all_ingredients = list(all_ingredients)

    # Check if list of ingredients is empty and exit if true
    if len(all_ingredients) == 0:
        print("No ingredients found. Returning to main menu.")
        return
    
    print("\nAll recipe ingredients:")
    # Display all ingredients with indexes
    for index, ingredient in enumerate(all_ingredients):
        print(f"{index}: {ingredient}")
    # Get user input for index parsing
    user_input = input("\nPick a number to select an ingredient or type 'quit' to exit: ")

    if user_input == 'quit':
        return
    
    # Get ingredient based on index
    try:
        ingredient_index = int(user_input)
        search_ingredient = all_ingredients[ingredient_index]
    except:
        # Handle input errors
        print("Input is incorrect. Please enter a valid number or type 'quit' to exit.")
        return
    
    # Search for rows in the table that contain search_ingredient
    query = '''SELECT name, ingredients, cooking_time, difficulty FROM Recipes WHERE ingredients LIKE %s
    '''
    search = f"%{search_ingredient}%"
    # Create a tuple with a single element, as MySQL connector cannot accept a string
    cursor.execute(query, (search,))
    matching_recipes = cursor.fetchall()

    # Display search results
    if matching_recipes:
        print(f"\nRecipes containing '{search_ingredient}':\n")
        for recipe in matching_recipes:
            name, ingredients, cooking_time, difficulty = recipe
            print(f"Name: {name}")
            print(f"Ingredients: {ingredients}")
            print(f"Cooking Time: {cooking_time} minutes")
            print(f"Difficulty: {difficulty}")
            print("\n---------------------------\n")
    else:
        print(f"No recipes found containing '{search_ingredient}'.")
        print("\n---------------------------\n")
        return

def update_recipe(conn, cursor):
    # Store all recipes
    cursor.execute("SELECT id, name FROM Recipes")
    all_recipes = cursor.fetchall()

    # Check if list of recipes is empty and exit if true
    if len(all_recipes) == 0:
        print("No recipes found. Returning to main menu.")
        return

    print("\nAll recipes:")
    # Display all recipes with their IDs and name
    for recipe in all_recipes:
        print(f"ID: {recipe[0]}, Name: {recipe[1]}")

    # Get recipe ID to update from user
    recipe_id = input("Enter the ID of the recipe to update: ")
    # Check if the user input ID matches any of the recipe IDs
    if not any(str(recipe[0]) == recipe_id for recipe in all_recipes):
        print("Invalid Recipe ID.")
        return
    
    # Ask the user for which column to update
    print("Which column would you like to update?")
    print("1. Name")
    print("2. Cooking Time")
    print("3. Ingredients")
    column_to_update = input("Enter the number for the column to update: ")
    
    # Map choice to column name and prompt for the new value
    column = None
    new_value = None

    if column_to_update == "1":
        column = "name"
        new_value = input("Enter the new name for the recipe: ")
        new_value = new_value.title()
        try:
            new_value = str(new_value)
        except ValueError:
            print("Invalid name.")
            return
    elif column_to_update == "2":
        column = "cooking_time"
        new_value = input("Enter the new cooking time (in minutes): ")
        try:
            new_value = int(new_value)
        except ValueError:
            print("Invalid cooking time.")
            return
    elif column_to_update == "3":
        column = "ingredients"
        ingredients = []
        print("Enter ingredients one by one (type 'done' to finish):")
        try:
            while True:
                ingredient = input("Ingredient: ")
                if ingredient.lower() == 'done':
                    break
                # Check if user entered nothing as ingredient
                elif ingredient == '':
                    print("Enter a valid ingredient.")
                    continue
                ingredients.append(ingredient.capitalize())

            # Check if no ingredients were entered
            if not ingredients:
                print("No ingredients entered. Returning to main menu.")
                return
            new_value = ", ".join(ingredients)
        except ValueError:
            print("Error adding ingredients.")
            print("\n---------------------------\n")
            return
    else:
        print("Invalid choice. Returning to main menu.")
        return

    # Update query for the chosen column
    query = f"UPDATE Recipes SET {column} = %s WHERE id = %s"
    cursor.execute(query, (new_value, recipe_id))
    conn.commit()

    # Recalculate difficulty
    if column in ["cooking_time", "ingredients"]:
        # Store cooking_time and ingredients
        cursor.execute("SELECT cooking_time, ingredients FROM Recipes WHERE id = %s", (recipe_id,))
        recipe_data = cursor.fetchone()

        # Handle if ingredients are None (no ingredients entered)
        ingredients_list = recipe_data[1].split(", ") if recipe_data[1] else []

        # Call function with cooking_time and ingredients properties
        # Store result in new_difficulty
        new_difficulty = calculate_difficulty(recipe_data[0], ingredients_list)

        # Update the difficulty in the database
        cursor.execute("UPDATE Recipes SET difficulty = %s WHERE id = %s", (new_difficulty, recipe_id))
        conn.commit()
        print("Recipe updated!")
        print("\n---------------------------\n")
    return

def delete_recipe(conn, cursor):
    # Store all recipes
    cursor.execute("SELECT id, name FROM Recipes")
    all_recipes = cursor.fetchall()

    # Check if list of recipes is empty and exit if true
    if len(all_recipes) == 0:
        print("No recipes found. Returning to main menu.")
        return

    print("\nAll recipes:")
    # Display all recipes with their IDs and name
    for recipe in all_recipes:
        print(f"ID: {recipe[0]}, Name: {recipe[1]}")

    while True:
        # Get recipe ID to delete from user
        try:
            recipe_id = input("Enter the ID of the recipe you want to DELETE or type 'quit' to exit: ")
            if recipe_id == 'quit':
                return
            else:
                recipe_id = int(recipe_id)
        except ValueError:
            print("Invalid input. Please enter a valid ID.")
            continue
        
        # Check if the user input ID matches any of the recipe IDs
        if any(recipe[0] == recipe_id for recipe in all_recipes):
            break
        if not any(recipe[0] == recipe_id for recipe in all_recipes):
            print("Please enter an existing Recipe ID.")
            continue
    # Query to delete recipe matching user input ID
    query = '''DELETE FROM Recipes WHERE id = %s
    '''
    cursor.execute(query, (recipe_id,))
    conn.commit()
    print("Recipe deleted!")
    print("\n---------------------------\n")

def calculate_difficulty(cooking_time, ingredients):
    if cooking_time < 10 and len(ingredients) < 4:
        difficulty = "Easy"
        return difficulty
    elif cooking_time < 10 and len(ingredients) >= 4:
        difficulty = "Medium"
        return difficulty
    elif cooking_time >= 10 and len(ingredients) < 4:
        difficulty = "Intermediate"
        return difficulty
    elif cooking_time >= 10 and len(ingredients) >= 4:
        difficulty = "Hard"
        return difficulty
    else:
        print("Something went wrong calculating recipe difficulty!")

def main_menu():
    while True:
        print("What would you like to do?\nEnter the number 1-4 or type 'quit' to exit the program.")
        print("1. Add recipe")
        print("2. Search for a recipe")
        print("3. Edit recipe")
        print("4. Delete recipe")
        choice = input("Your choice: ")

        if choice == "1":
            create_recipe(conn, cursor)
        elif choice == "2":
            search_recipe(conn, cursor)
        elif choice == "3":
            update_recipe(conn, cursor)
        elif choice == "4":
            delete_recipe(conn, cursor)
        elif choice.lower() == "quit":
            print("Exiting the program.")
            conn.close()
            break
        else:
            print("Invalid input. Please try again.")

main_menu()