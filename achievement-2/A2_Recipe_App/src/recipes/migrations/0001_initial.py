# Generated by Django 4.2.16 on 2024-12-02 07:21

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('cooking_time', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(300)])),
                ('difficulty', models.CharField(choices=[('easy', 'Easy'), ('medium', 'Medium'), ('intermediate', 'Intermediate'), ('hard', 'Hard')], default='easy', max_length=12)),
                ('ingredients', models.TextField(help_text="Enter ingredients separated by commas, e.g., 'flour, sugar, eggs'")),
            ],
        ),
    ]