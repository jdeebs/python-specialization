# Initialize empty lists
recipes_list = []
ingredients_list = []

# Define function to take a recipe
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
        if ingredient not in ingredients_list:
            ingredients_list.append(ingredient)

    # Append the recipe to recipes_list
    recipes_list.append(recipe)

# Conditionally set cooking difficulty based on cooking time and ingredients
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

print("Recipe: " + recipes_list['name'],
      "Cooking Time (min): " + recipes_list['cooking_time'],
      "Ingredients: ",
      recipes_list['ingredients'],
      "Difficulty level: " + recipes_list['difficulty']
      )