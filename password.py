class User :
    """
    Class that generates new instances of users
    """
    user_list = []

    def __init__ (self,user_name,accountname,email,password):

        """
        __init__ method that helps us define properties for our objects.

        Args:
            name: New name of the user.
            accountname : New name of the account.
            email : New contact email address.
            password : New password of the user.
        """
        self.user_name = user_name
        self.accountname = accountname
        self.email = email
        self.password = password

    def save_user(self):
        """
        save_user method saves contact objects into user_list
        """
        User.user_list.append(self)

    def delete_user(self):
        """
        delete_user method deletes user objects from our user_list
        """
        User.user_list.remove(self)

    @classmethod
    def find_by_accountname(cls,accountname):
        """
        Method that takes in an account name and returns an account that matches that account name
    
        Args:
            account name: Account name to search for
        Returns :
            Account of user that matches the account name.
        """
        for user in cls.user_list:
            if user.accountname == accountname:
                return user

    @classmethod
    def user_exist(cls,email):
        """
        Method that checks if a user exists
        Args:
            email: Email to search if it exists
        Returns :
            Boolean: True or false depending if the contact exists 
        """
        for user in cls.user_list:
            if user.email == email:
                return True

        return False