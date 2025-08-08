import os
import time

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

class User:
    def __init__(self, name, last_name, email, password, status= 'inactive'):
        self.name = name
        self.last_name = last_name
        self.email = email
        self.password = password
        self.status = status

    def display(self):
        
        print(f"\nFirst name: {self.name}")
        print(f"\nLast name: {self.last_name}")
        print(f"\nEmail: {self.email}")
        print(f"\nPassword: {self.password}")
        print(f"\nStatus: {self.status}\n")
        
def create_user():
    name = input("\nEnter First Name: ")
    last_name = input("\nEnter Last Name: ")
    email = input("\nEnter Email: ")
    password = input("\nEnter Password: ")
    status = input("\nEnter status: ")

    if status == '':
        status = 'inactive'

    return User(name, last_name, email, password, status)

users = []

while True:

    print('\nWelcome to user management ')
    print("\n1.Add a new user")
    print('2.Display all users')
    print('3.Exit')

    choice = input("\nEnter your choice: ")

    if choice == '1':
        users.append(create_user())
        time.sleep(1)
        print("\nUser added successfully")
        time.sleep(2)
        
    elif choice == '2':
        
        if users:

            clear()
            print(f"\n{'*' * 50}Displaying users{'*' * 50}")

            for user in users:
                user.display()
                print('*' * 30)
            time.sleep(4)
        else:
            print("We can't find anyone. add user and try again.")
            time.sleep(2)

    elif choice == '3':
        print("\nExiting the program ....")
        break
    else:
        print("\ninvalid choice. Try again.")
        time.sleep(2)

