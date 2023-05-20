from Contacts.contact import Contact
from Contacts.storage import Storage
from art import *
from colorama import Fore 
# for playing note.wav file
tprint(Fore.BLACK +"Welcome to Contact info:",font="cybermedum")
def add_contact(storage):
    try:
        name = input( Fore.GREEN +"Enter the name: ")
        phone = input(Fore.GREEN +"Enter the phone number: ")
        phone = int(phone)
        email = input(Fore.GREEN +"Enter the email address: ")
    except ValueError as e:
        print(Fore.RED + f"Error: {e}")

    contact = Contact(name, phone, email)
    storage.add_contact(contact)
    print(f"Added contact: {contact}")

def remove_contact(storage):
    name = input("Enter the name of the contact to remove: ")
    try:
        storage.remove_contact(name)
        print(Fore.RED + f"Removed contact: {name}")
    except ValueError as e:
        print(Fore.RED + f"Error: {e}")

def find_contact(storage):
    name = input("Enter the name of the contact to find: ")
    contact = storage.find_contact(name)

    if contact:
        print(f"Found contact: {contact}")
    else:
        print(Fore.RED + f"No contact found with name '{name}'")

def main():
    storage = Storage()
    actions = {
        "add": add_contact,
        "remove": remove_contact,
        "find": find_contact,
    }
#Main funcation
    while True:
        action = input(Fore.YELLOW +"Choose an action (add, remove, find, quit): ").lower()

        if action == "quit":
            break

        action_func = actions.get(action)

        if action_func:
            action_func(storage)
        else:
            print(Fore.RED + f"Unknown action '{action}'. Please try again.")

if __name__ == "__main__":
    main()