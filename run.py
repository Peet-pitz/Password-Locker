#!/usr/bin/env python3.6

from password import User
import random

def create_user(user_name,account,email,password):
    """
    function to create new user
    """
    new_user = User(user_name,account,email,password)
    return new_user

def save_users(user):
    """
    Function to save user
    """
    user.save_user()

def del_user(user):
    """
    Function to delete user
    """
    user.delete_user()

def find_user(account_name):
    """
    Function that finds a user by account name and returns the user
    """
    return User.find_by_account_name(account_name)
def check_existing_user(account_name):
    return User.display_users()

def display_user():
    """
    Function that returns all saved users
    """
    return User.display_users()

def main():
    print("Hello Welcome to your Password Locker.Enter user name")
    user_name = input()

    print(f"What's good {user_name}." )
    print('\n')

    while True:
            print("Use these short codes : ca - create new account, da - display accounts, fa - find account, dl - delete account, gp - generate password, ex - exit ")

            short_code = input().lower()

            if short_code == 'ca':
                print("New Account")
                print("-"*10)

                print("user_name....")
                user_name= input()

                print("account....")
                account= input()

                print("Email....")
                email= input()

                print("Password....")
                password= input()

                save_users(create_user(user_name,account,email,password))
                print('\n')
                print(f"New account {account} created")
                print('\n')

            elif short_code == 'da':

                    if display_user():
                            print("Here is a list of all your accounts")
                            print('\n')

                            for user in display_user():
                                    print(f"{user.account_name} {user.password}")
                            print('\n')

                    else:
                            print('\n')
                            print("You dont seem to have any accounts saved yet")
                            print('\n')

            elif short_code == 'fa':
                    print("Enter the account you want to search for")

                    search_user = input()
                    if check_existing_user(search_user):
                            search_user = find_user(search_user)
                            print(f"{search_user.account} {search_user.password}")

                            print(f"Account....{search_user.account}")
                            print(f"Email address....{search_.email}")
                    else:
                            print("That user does not exist")

            elif short_code == 'gp':
                    print("Enter new account to generate password")
                    account_name = input()
                    password = random.randint(0000,9999)
                    print("Your password is")
                    password = input(account_name)

            elif short_code == "ex":
                    print("See you soon....")
                    break
            else:
                    print("I really didn't get that. Please use the short codes")

if __name__ == '__main__':

    main()

                    





