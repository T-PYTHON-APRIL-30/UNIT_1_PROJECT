from input_validator import validate_input,validate_password
from password_manger import Password
import os.path
import pickle

def add_password():
    name = validate_input("Enter password name: ")
    username = validate_input("Enter username: ")
    password = validate_password("Enter password: ")
    file_name = validate_input("Enter file name: ")
    master_password = validate_input("Enter master password: ")

    new_password = Password(name, username, password,file_name)
    new_password.encrypt_password(master_password)
    if os.path.exists(file_name):
        with open(file_name, "rb") as file:
            passwords = pickle.load(file)   
        
    else:
        passwords = []

    passwords.append(new_password)
    with open(file_name, "wb") as file:
        pickle.dump(passwords, file)
        
    print("Password saved successfully!")
             
def view_passwords():
    file_name = validate_input("Enter file name: ")

    if not os.path.exists(file_name):
        print("No file found.")
        return
    
    master_password = validate_input("Enter master password: ")

    with open(file_name, "rb") as file:
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
    file_name = validate_input("Enter file name: ")

    if not os.path.exists(file_name):
        print("No file found")
        return
    password_name = validate_input("Enter password name: ")
    master_password = validate_input("Enter master password: ")

    with open(file_name,"rb") as file:
        passwords=pickle.load(file)
        
    for line,password in enumerate(passwords):
        try:
            password.decrypt_password(master_password)
            if password.name == password_name:
                del passwords[line]
                with open(file_name,"wb")as file:
                    pickle.dump(passwords,file)
                print("Password deleted successfully!")
                return
            password.encrypt_password(master_password)
        except ValueError:
            print("Incorrect master password.")
            return
    print("Password not found.")


while True:
    print("Welcome to the Password Manager!")
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
        