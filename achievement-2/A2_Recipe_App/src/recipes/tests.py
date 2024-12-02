from django.test import TestCase
from .models import Recipe
# Import validators
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your tests here.


class RecipeModelTest(TestCase):
    def setUpTestData():
        # Set up test data object
        Recipe.objects.create(
            name='Pancakes',
            cooking_time=10,
            difficulty='easy',
            ingredients='flour, sugar, eggs'
        )

    def test_name(self):
        # Get recipe object to test
        recipe = Recipe.objects.get(id=1)

        # Get metadata for 'name' field and use to query its data
        field_label = recipe._meta.get_field('name').verbose_name

        # Compare the name to expected result
        self.assertEqual(field_label, 'name')

    def test_name_max_length(self):
        recipe = Recipe.objects.get(id=1)

        # Get field metadata
        max_length = recipe._meta.get_field('name').max_length

        # Assert that the max length is 120
        self.assertEqual(max_length, 120)

        # Compare the recipes name to <= 120
        self.assertTrue(len(recipe.name) <= 120)

    def test_cooking_time_validators(self):
        recipe = Recipe.objects.get(id=1)

        # Get field metadata
        cooking_time = recipe._meta.get_field('cooking_time')

        # Extract validators from cooking field
        validators = cooking_time.validators
        # Check if MaxValueValidator is present and its value is 300
        max_value = next(
            (v.limit_value for v in validators if isinstance(v, MaxValueValidator)), None)
        self.assertIsNotNone(
            max_value, "MaxValueValidator is missing from the cooking_time field.")
        self.assertEqual(max_value, 300)

        # Check if MinValueValidator is present and its value is 1
        min_value = next(
            (v.limit_value for v in validators if isinstance(v, MinValueValidator)), None)
        self.assertIsNotNone(
            min_value, "MinValueValidator is missing from the cooking_time field.")
        self.assertEqual(min_value, 1)

    def test_difficulty_max_length(self):
        recipe = Recipe.objects.get(id=1)

        # Get field metadata
        max_length = recipe._meta.get_field('difficulty').max_length

        # Assert that the max length is 12
        self.assertEqual(max_length, 12)

        # Compare the recipes difficulty to <= 12
        self.assertTrue(len(recipe.difficulty) <= 12)

    def test_difficulty_choices_length(self):
        recipe = Recipe.objects.get(id=1)

        # Get difficulty choices
        choices = recipe._meta.get_field('difficulty').choices

        # Check that the amount of choices is 4
        self.assertEqual(len(choices), 4)

    def test_ingredients_format(self):
        recipe = Recipe.objects.get(id=1)

        # Get ingredients
        ingredients = recipe.ingredients

        # Check if the ingredients are comma-separated
        self.assertTrue(
            # Use all() for cases of empty string ingredients (they return false)
            all(ingredient.strip() for ingredient in ingredients.split(",")),
            "Ingredients are not properly comma-separated."
        )
