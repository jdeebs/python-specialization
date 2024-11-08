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
            return difficulty
               ''')

def create_recipe(conn, cursor):
    print("Enter your recipe info")

    # Get user input for name and cooking time
    name = str(input("Recipe name: "))
    cooking_time = int(input("Cooking time (in minutes): "))

    # Get ingredients as a list
    ingredients = []
    print("Enter ingredients one by one (type 'done' to finish): ")
    # Append each ingredient until user types done
    while True:
        ingredient = str(input("Ingredient: "))
        if ingredient.lower() == 'done':
            break
        ingredients.append(ingredient)

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

def search_recipe(conn, cursor):
    # Store entire ingredients column w/ tuples on each row containing specific recipe ingredients
    results = cursor.execute("SELECT ingredients FROM Recipes")
    # Use a set to handle duplicates
    all_ingredients = set()

    # Iterate over each row in ingredients column
    for row in results:
        # Split the string by comma and space to get individual ingredients
        ingredients = row[0].split(", ")
        # Add each ingredient to the set, ignoring duplicates
        all_ingredients.update(ingredients)

    all_ingredients = list(all_ingredients)

    """
Display all the ingredients that you've found so far to the user, and allow them to pick a number corresponding to the ingredient in order to begin a search. Store the ingredient to be searched for into a variable called search_ingredient.
To search for rows in the table that contain search_ingredient within the ingredients column, use the WHERE statement with the LIKE operator: SELECT <columns to be displayed> FROM <table> WHERE <search column> LIKE <search pattern>.
    """

def update_recipe(conn, cursor):
    return

def delete_recipe(conn, cursor):
    return

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
    while(choice != "quit"):
        print("What would you like to do? Pick a choice!")
        print("1. Add recipe")
        print("2. Search for a recipe")
        print("3. Edit recipe")
        print("4. Delete recipe")
        print("Type 'quit' to exit the program.")
        choice = input("Your choice: ")

        if choice == "1":
            create_recipe()
        elif choice == "2":
            search_recipe()
        elif choice == "3":
            update_recipe()
        elif choice == "4":
            delete_recipe()
        elif choice == "quit":
            break
        else:
            print("Invalid input. Please try again.")
            continue

main_menu(conn, cursor)