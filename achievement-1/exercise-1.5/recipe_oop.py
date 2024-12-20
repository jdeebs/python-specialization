class Recipe(object):
    # Class variable to store all ingredients
    all_ingredients = []
    # Init attributes
    def __init__(self, name, *ingredients, cooking_time):
        self.name = name
        self.ingredients = list(ingredients) # Variable-length list
        self.cooking_time = cooking_time
        self.difficulty = self.calculate_difficulty(cooking_time, ingredients)

    # Methods
    def get_name(self):
        return self.name
    
    def get_cooking_time(self):
        return self.cooking_time
    
    def get_ingredients(self):
        return self.ingredients
    
    def get_difficulty(self):
            return self.difficulty
    
    def add_ingredients(self, *ingredients):
        self.ingredients.extend(ingredients)
        self.update_all_ingredients()
    
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
        return difficulty


    def search_ingredient(self, ingredient):
        return ingredient in self.ingredients
    
    def update_all_ingredients(self):
        for ingredient in self.ingredients:
            if ingredient not in Recipe.all_ingredients:
                Recipe.all_ingredients.append(ingredient)
    
    def display_recipe(self):
        # Format ingredients list with a new line per ingredient
        ingredients_formatted = "\n".join(self.ingredients)

        recipe_details = (
            f"--------------------------\n"
            f"Recipe: {self.name}\n"
            f"Cooking Time (min): {self.cooking_time}\n"
            f"Ingredients:\n{ingredients_formatted}\n"
            f"Difficulty level: {self.difficulty}"
            )
        print(recipe_details)
    
    @classmethod
    def recipe_search(cls, data, search_term):
        # Iterate over each recipe
        for recipe in data:
            # If search_ingredient() returns true, display that recipe
            if recipe.search_ingredient(search_term):
                recipe.display_recipe()

# Define recipes
tea = Recipe("Tea", "Tea Leaves", "Sugar", "Water", cooking_time=5)
coffee = Recipe("Coffee", "Coffee Powder", "Sugar", "Water", cooking_time=5)
cake = Recipe("Cake", "Sugar", "Butter", "Eggs", "Vanilla Essence", "Flour", "Baking Powder", "Milk", cooking_time=50)
banana_smoothie = Recipe("Banana Smoothie", "Bananas", "Milk", "Peanut Butter", "Sugar", "Ice Cubes", cooking_time=5)

# Display recipes
tea.display_recipe()
coffee.display_recipe()
cake.display_recipe()
banana_smoothie.display_recipe()

# Wrap the recipes into a list
recipes_list = [tea, coffee, cake, banana_smoothie]

# Search for recipes that contain specific ingredients
print("\nRecipes containing 'Water':")
Recipe.recipe_search(recipes_list, "Water")

print("\nRecipes containing 'Sugar':")
Recipe.recipe_search(recipes_list, "Sugar")

print("\nRecipes containing 'Bananas':")
Recipe.recipe_search(recipes_list, "Bananas")
