import unittest
from password import User

class TestUser(unittest.TestCase):

    """
    Test class that defines test cases for the user class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    """
    def setUp(self):
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

    def test_save_user(self):
        """
        test_save_user test case to test if the user object is saved into the user list.
        """
        self.new_user.save_user()
        self.assertEqual(len(User.user_list),1)

if __name__ == '__main__':
    unittest.main()
