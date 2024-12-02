from django.test import TestCase
from .models import Book

# Create your tests here.


class BookModelTest(TestCase):
    def setUpTestData():
        # Set up non-modified objects used by all test methods
        Book.objects.create(
            name='Pride and Prejudice', author_name='Jane Austen', genre='classic', book_type='hardcover',
            price='23.71'
        )

    def test_book_name(self):
        # Get book object to test
        book = Book.objects.get(id=1)

        # Get the metadata for the 'name' field and use it to query its data
        field_label = book._meta.get_field('name').verbose_name

        # Compare the value to the expected result
        self.assertEqual(field_label, 'name')

    def test_author_name_max_length(self):
        # Get book object to test
        book = Book.objects.get(id=1)

        # Get the metadata for the 'author_name' field
        max_length = book._meta.get_field('author_name').max_length

        # Assert that the max_length is 120
        self.assertEqual(max_length, 100)

        # Compare the authors name value to <= 120
        self.assertTrue(len(book.author_name) <= 120)
