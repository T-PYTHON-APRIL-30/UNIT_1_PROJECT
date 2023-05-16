from input_validator import validate_string_input
from password_manger import Password
import os.path
import pickle

PASSWORD_FILE = "passwords.txt"
def add_password():
    name = validate_string_input("Enter password name: ")
    username = validate_string_input("Enter username: ")
    password = validate_string_input("Enter password: ")
    master_password = validate_string_input("Enter master password: ")

    new_password = Password(name, username, password)
    new_password.encrypt_password(master_password)
    if os.path.exists(PASSWORD_FILE):
        with open(PASSWORD_FILE, "rb") as file:
            passwords = pickle.load(file)   
        
    else:
        passwords = []

    passwords.append(new_password)
    with open(PASSWORD_FILE, "wb") as file:
        pickle.dump(passwords, file)
        

    print("Password saved successfully!")
             

def view_passwords():
    if not os.path.exists(PASSWORD_FILE):
        print("No passwords found.")
        return
    
    master_password = validate_string_input("Enter master password: ")

    with open(PASSWORD_FILE, "rb") as file:
        passwords = pickle.load(file)

    print("Passwords:")
    for password in passwords:
        try:
            password.decrypt_password(master_password)
            print(f"- {password.name}")
            print(f"  - Username: {password.username}")
            print(f"  - Password: {password.password}")
            password.encrypt_password(master_password)
        except ValueError:
            print("Incorrect master password. Exiting.")
            return
        

def delete_password():
     pass


while True:
    user_choose = input("Enter a command (a/v/d/q): ").lower()

    if user_choose == "a":
        add_password()
    elif user_choose == "v":
        view_passwords()
    elif user_choose == "d":
        delete_password()
    elif user_choose == "q":
        print("Goodbye!")
        break
    else:
        print("Invalid command. Please try again.")
        