from input_validator  import validate_input,validate_password
from password_manger import Password
import pickle
import os.path

def add_password():
    """Adds a new password to a file, if it is found,
      and if it is not found, create a new file"""
    name = validate_input("Enter app name: ")
    username = validate_input("Enter username: ")
    password = validate_password("Enter password: ")
    file_name = validate_input("Enter file name: ")
    master_password = validate_input("Enter master key: ")

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
    
    master_password = validate_input("Enter master key: ")

    with open(file_name, "rb") as file:
        passwords = pickle.load(file)
    
    if not passwords:
        print("No Passwords Found.")
        return

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
        except:
            print("password not found")
            return
        

def delete_password():
    file_name = validate_input("Enter file name: ")

    if not os.path.exists(file_name):
        print("No file found")
        return
    password_name = validate_input("Enter app name: ")
    master_password = validate_input("Enter master key: ")

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
