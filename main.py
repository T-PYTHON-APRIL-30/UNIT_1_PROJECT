from command import *


print("Welcome to the Password Manager!")
print(f"a: Add a new password\nv: View passwords\nd: Delete a password\nq: Quit the program")

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
        