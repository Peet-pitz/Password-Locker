class User :
    """
    Class that generates new instances of users
    """

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