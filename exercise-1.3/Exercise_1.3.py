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

for _ in range(n):
    # Run take_recipe and store its output
    recipe = take_recipe()

    for ingredient in recipe['ingredients']:
        if ingredient not in ingredients_list:
            ingredients_list.append(ingredient)
    
    # Append the recipe to recipes_list
    recipes_list.append(recipe)