import pickle

def display_recipe(recipe):
    # Format ingredients list with a new line per ingredient
    ingredients_formatted = "\n".join(recipe['ingredients'])

    recipe_details = (
        f"Recipe: {recipe['name']}\n"
        f"Cooking Time (min): {recipe['cooking_time']}\n"
        f"Ingredients:\n{ingredients_formatted}\n"
        f"Difficulty level: {recipe['difficulty']}\n"
    )
    print(recipe_details)

def search_ingredient(data):
    # Display all ingredients with indexes
    for index, ingredient in enumerate(data['all_ingredients']):
        print(f"{index}: {ingredient}")
    try:
        # Get user input for index parsing
        ingredient_index = int(input("Pick a number to select your ingredient: "))
        # Get ingredient based on index
        ingredient_searched = data['all_ingredients'][ingredient_index]
    except:
        # Handle input errors
        print("Input is incorrect")
    else:
        # Iterate through all recipes to find and print matches
        for recipe in data['recipes_list']:
            if ingredient_searched in recipe['ingredients']:
                print(recipe)