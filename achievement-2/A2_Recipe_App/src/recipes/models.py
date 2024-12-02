from django.db import models
# Import validators
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
difficulty_choices = (
    ('easy',
     'Easy'),
    ('medium',
     'Medium'),
    ('intermediate',
     'Intermediate'),
    ('hard',
     'Hard')
)


class Recipe(models.Model):
    name = models.CharField(max_length=120)

    cooking_time = models.IntegerField(validators=[
        MinValueValidator(1),
        MaxValueValidator(300)
    ])

    difficulty = models.CharField(
        max_length=12, choices=difficulty_choices, default='easy')

    ingredients = models.TextField(
        help_text="Enter ingredients separated by commas, e.g., 'flour, sugar, eggs'"
    )

    def __str__(self):
        return str(self.name)