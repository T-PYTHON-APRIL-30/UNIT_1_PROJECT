import my_functions
import my_files
def menu():
    print("{:^30}".format("hello threre"))
    print("1. Create a new password")
    print("2. Decrypt your password")
    print("3. More options")
    print("4. Exit")

    choice = input("Please enter your choice: ")
    if choice == "1":
        print("You chose creating a new password.")
        try:
            my_functions.new_user()
            menu()
        except:
            print("you didn't enter the correct input")
            #my_functions.new_user()
            menu()

    elif choice == "2":
        print("You chose drcrypting your password.")
        my_functions.old_user()
        menu()
    elif choice == "3":
        submenu()
    elif choice == "4":
        print("Thank you for using this program")
        exit()
    else:
        print("Invalid choice.")
        menu()

def submenu():
    print("{:^30}".format("More options"))
    print("1. Display passwords")
    print("2. Display keys")
    print("3. Back")

    subchoice = input("Enter choice: ")
    if subchoice == "1":
        user_input=input("Please enter your username: ")
        my_files.show_passwords(user_input)
        submenu()
    elif subchoice == "2":
        user_input=input("Please enter your username: ")
        my_files.show_keys(user_input)
        submenu()
    elif subchoice == "3":
        menu()
    else:
        print("Invalid choice.")
        submenu()

menu()