import pickle

# Initialize empty lists
recipes_list = []
all_ingredients = []
# Combine lists into a dictionary containing two key-value pairs
data = {
    'recipes_list': recipes_list,
    'all_ingredients': all_ingredients
}

def take_recipe():
    print("Enter your recipe info")

    # Get user input for each recipe detail
    name = str(input("Recipe name: "))
    cooking_time = int(input("Cooking time (in minutes): "))

    # Get ingredients as a list
    ingredients = []
    print("Enter ingredients one by one (type 'done' to finish): ")
    # Append each ingredient until user types done
    while True:
        ingredient = input("Ingredient: ")
        if ingredient.lower() == 'done':
            break
        ingredients.append(ingredient)

    # Recipe dictionary
    recipe = {
        'name': name,
        'cooking_time': cooking_time,
        'ingredients': ingredients
    }
    return recipe

n = int(input("How many recipes would you like to enter?: "))

# Prompt for amount of new recipes based on what the user entered
for _ in range(n):
    # Run take_recipe and store its output
    recipe = take_recipe()

    for ingredient in recipe['ingredients']:
        if ingredient not in all_ingredients:
            all_ingredients.append(ingredient)

    # Append the recipe to recipes_list
    recipes_list.append(recipe)

# Conditionally set cooking difficulty based on cooking time and ingredients
def calc_difficulty():
    for recipe in recipes_list:
        if recipe['cooking_time'] < 10 and len(recipe['ingredients']) < 4:
            difficulty = "Easy"
        elif recipe['cooking_time'] < 10 and len(recipe['ingredients']) >= 4:
            difficulty = "Medium"
        elif recipe['cooking_time'] >= 10 and len(recipe['ingredients']) < 4:
            difficulty = "Intermediate"
        elif recipe['cooking_time'] >= 10 and len(recipe['ingredients']) >= 4:
            difficulty = "Hard"

        # Add difficulty to recipe dictionary item
        recipe['difficulty'] = difficulty

# Call function to calculate difficulty and append it to recipe
calc_difficulty()

filename = input("Enter the filename where you've stored your recipes: ")
try:
    # Open file in binary read mode
    with open(filename, 'rb') as file:
        # Attempt to load data from file
        data = pickle.load(file)
        print("Data loaded successfully.")
except FileNotFoundError:
    # If file doesn't exist, initialize with empty lists
    data = {
        'recipes_list': [],
        'all_ingredients': []
        }
    print("File not found.")
except:
    print("An unexpected error occurred.")
else:
    pass
finally:
    # Update recipes and ingredients in data dictionary
    data['recipes_list'].extend(recipes_list)
    # Only add ingredients that aren't in data['all_ingredients']
    data['all_ingredients'].extend([ingredient for ingredient in all_ingredients if ingredient not in data['all_ingredients']])

    # Save updated data to file
    with open(filename, 'wb') as file:
        pickle.dump(data, file)

    print("Data saved successfully!")