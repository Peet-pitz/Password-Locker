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

    def tearDown(self):
        """
        tearDown method that does clean up after each test case has run
        """
        User.user_list = []

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

    def test_save_multiple_user(self):
        """
        test_save_multiple_user to check if we can save multiple user objects to our user_list
        """
        self.new_user.save_user()
        test_user = User("Test","account","test@gmail.com","new pass")
        test_user.save_user()
        self.assertEqual(len(User.user_list),2)

    def test_delete_user(self):
        """
        test_delete_user to test if we can delete a user from our user list
        """
        self.new_user.save_user()
        test_user = User("Test","account","test@gmail.com","new pass")
        test_user.save_user()

        self.new_user.delete_user()
        self.assertEqual(len(User.user_list),1) 

    def test_find_user_by_accountname(self):
        """
        test to see if we can find a user by account name and display information
        """
        self.new_user.save_user()
        test_user = User("Test","account","test@gmail.com","new pass")
        test_user.save_user()

        found_user = User.find_by_accountname("account")
        self.assertEqual(found_user.email,test_user.email)

    def test_user_exists(self):
        """
        test to checkif we can return Boolean if we find the user
        """
        self.new_user.save_user()
        test_user = User("Test","account","test@gmail.com","new pass")
        test_user.save_user()

        user_exists = User.user_exist("test@gmail.com")
        self.assertTrue(user_exists)

    def test_display_all_users(self):
        """
        method that returns a list of all users saved
        """
        self.assertEqual(User.display_user(),User.user_list)

if __name__ == '__main__':
    unittest.main()
