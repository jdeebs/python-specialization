from django.test import TestCase
from .models import User

# Create your tests here.


class UserModelTest(TestCase):
    # Set up non-modified user object to be used by test
    def setUpTestData():
        User.objects.create(
            name='Chef Boyardee'
        )

    def test_user_name(self):
        # Get user object
        user = User.objects.get(id=1)

        # Get metadata for the 'name' field and use to query its data
        field_label = user._meta.get_field('name').verbose_name

        # Compare the value to the expected result
        self.assertEqual(field_label, 'name')

    def test_user_name_max_length(self):
        user = User.objects.get(id=1)

        # Get the metadata for the 'name' field
        max_length = user._meta.get_field('name').max_length

        # Assert that the max length is 120
        self.assertEqual(max_length, 120)

        # Compare the name value to <= 120
        self.assertTrue(len(user.name) <= 120)