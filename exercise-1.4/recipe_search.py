import pickle

def display_recipe(recipe):
    # Format ingredients list with a new line per ingredient
    ingredients_formatted = "\n".join(recipe['ingredients'])

    recipe_details = (
        f"--------------------------\n"
        f"Recipe: {recipe['name']}\n"
        f"Cooking Time (min): {recipe['cooking_time']}\n"
        f"Ingredients:\n{ingredients_formatted}\n"
        f"Difficulty level: {recipe['difficulty']}"
    )
    print(recipe_details)

def search_ingredient(data):
    # Display all ingredients with indexes
    for index, ingredient in enumerate(data['all_ingredients']):
        print(f"{index}: {ingredient}")
    try:
        # Get user input for index parsing
        ingredient_index = int(input("\nPick a number to select your ingredient: "))
        # Get ingredient based on index
        ingredient_searched = data['all_ingredients'][ingredient_index]
    except:
        # Handle input errors
        print("Input is incorrect")
    else:
        print(f"Recipes that include {ingredient_searched.lower()}:")
        # Iterate through all recipes to find and print the formatted matches with display_recipe function
        for recipe in data['recipes_list']:
            if ingredient_searched in recipe['ingredients']:
                display_recipe(recipe)

filename = input("Enter the filename where you've stored your recipes: ")
try:
    with open(filename, 'rb') as file:
        data = pickle.load(file)
        print("Data loaded successfully!")
except:
    print("An unexpected error occurred.")
else:
    search_ingredient(data)
    print("\nSearch concluded. Goodbye.")