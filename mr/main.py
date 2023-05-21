from Contacts.contact import Contact
from Contacts.storage import Storage
from art import *
from colorama import Fore
# for playing note.wav file
tprint(Fore.BLACK +"Welcome to Contact info:",font="cybermedum")

#Enter info to storage
def add_contact(storage):
    try:
        name = input( Fore.GREEN +"Enter the name: ")
        phone = input(Fore.GREEN +"Enter the phone number: ")
        email = input(Fore.GREEN +"Enter the email address: ")
    except ValueError as e:
        print(Fore.RED + f"Error: {e}")
#massage to add contant
    contact = Contact(name, phone, email)
    storage.add_contact(contact)
    print(f"Added contact: {contact}")
# search for name and remove id exisit
def remove_contact(storage):
    name = input("Enter the name of the contact to remove: ")
    #Holding excp
    try:
        storage.remove_contact(name)
        print(Fore.RED + f"Removed contact: {name}")
    except ValueError as e:
        print(Fore.RED + f"Error: {e}")
# search and display
def find_contact(storage):
    name = input("Enter the name of the contact to find: ")
    contact = storage.find_contact(name)

    if contact:
        print(Fore.BLUE + f"Found contact: {contact}")
    else:
        print(Fore.RED + f"No contact found with name '{name}'")
   
'''def display_contact():
    print(Contact.items())
    print("Name\t\tContact Number")
    for key in Contact:
        print("{}\t\t{}".format(key,Contact.get(key)))  '''      

def main():
    storage = Storage()
    actions = {
        "add": add_contact,
        "delete": remove_contact,
        "search": find_contact,
    }
#Main funcation
    while True:
        action = input(Fore.YELLOW +"Choose an action \n\n 1. Add new contact  \n\n 2.Delete contact  \n\n 3.Search contact  \n\n 4.Quit \n  ").lower()

        if action == "quit":
            break

        action_func = actions.get(action)

        if action_func:
            action_func(storage)
        else:
            print(Fore.RED + f"Unknown action '{action}'. Please try again.")

if __name__ == "__main__":
    main()