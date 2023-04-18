import unittest

from week9.utils.utils_dashboard import increment_visit


class TestIncrementVisit(unittest.TestCase):

    def test_increment_visit(self):
        # Define a sample user
        user = {"name": "John", "age": 30, "visits": 5}

        # Call the function to increment visits
        user = increment_visit(user)

        # Check that visits have been incremented by 1
        self.assertEqual(user["visits"], 6)

        # Check that other properties of the user have not been modified
        self.assertEqual(user["name"], "John")
        self.assertEqual(user["age"], 30)
