import pickle

recipe = {
    'name': 'Tea',
    'ingredients': ["Tea leaves", "Water", "Sugar"],
    'cooking_time': 5,
    'difficulty': 'easy'
}

# Create/open binary file with write method
recipe_file = open('recipedetail.bin', 'wb')

# Convert recipe object to binary and store it in recipedetail.bin
pickle.dump(recipe, recipe_file)

# Close file to ensure data is saved and resources are released
recipe_file.close()

# Load data back into script
with open('recipedetail.bin', 'rb') as recipe_file:
    recipe = pickle.load(recipe_file)

# Print formatted recipe details
print("Ingredient name: " + recipe['name'])
print("Ingredients: " + ", ".join(recipe['ingredients']))
print("Cooking Time: " + str(recipe['cooking_time']) + " minutes")
print("Difficulty: " + recipe['difficulty'].capitalize())