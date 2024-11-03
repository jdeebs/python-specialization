class Recipe(object):
    # Class variable to store all ingredients
    all_ingredients = []
    # Init attributes
    def __init__(self, name, *ingredients, cooking_time):
        self.name = name
        self.ingredients = list(ingredients) # Variable-length list
        self.cooking_time = cooking_time
        self.calculate_difficulty()

    # Methods
    def get_name(self):
        return self.name
    
    def get_cooking_time(self):
        return self.cooking_time
    
    def get_ingredients(self):
        return self.ingredients
    
    def get_difficulty(self):
        if self.difficulty is None:
            self.calculate_difficulty(self.cooking_time, self.ingredients)
            return self.difficulty
        else:
            print("Error getting recipe difficulty.")
    
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

        # Update difficulty based on above conditions
        self.difficulty = difficulty

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
    
    def recipe_search(self, data, search_term):
        # Iterate over each recipe
        for recipe in data:
            # If search_ingredient() returns true, display that recipe
            if recipe.search_ingredient(search_term):
                recipe.display_recipe()

