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