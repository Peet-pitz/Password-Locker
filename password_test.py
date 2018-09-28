import unittest
from password import User

class TestUser(unittest.TestCase):

    """
    Test class that defines test cases for the user class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    """
    def setup(self):
        """
        Set up method to run before each rest cases.
        """
        self.new_user = User("Pitz","Facebook","@pitz.com","Pass123")

    def test_init(self):
        """
        test_init test case to test if the object is initialised properly
        """

        self.assertEqual(self.new_user.user_name,"Pitz")
        self.assertEqual(self.new_user.accountname,"Facebook")
        self.assertEqual(self.new_user.email,"@pitz.com")
        self.assertEqual(self.new_user.password,"Pass123")

if __name__ == '__main__':
    unittest.main()
