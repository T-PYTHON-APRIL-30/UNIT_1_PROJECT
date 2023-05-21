# UNIT_1_PROJECT

#### Usage :
 Explain to the user how to use your project . 
 for example:
 - type in search product_name to search for a product.
 - type in list_products to show all the products in the grocery.
 - type in show product_name to get information about this product.
 - type in buy product_name to buy the product . 
 - and so on...


### Project Structure
 - The Password Manager project is structured as follows:


main.py: The main module of the project. It contains the code for the command-line interface and the logic for managing passwords.
password.py: The module that defines the Password class.
encryption.py: A module that contains functions for encrypting and decrypting data.
input_validator.py: A module that contains a function for validating user input.

### Function
### The Password class has the following attributes:

name: A string representing the name of the password.
username: A string representing the username associated with the password.
password: A string representing the password.
file name: representing the File

### The Password class has the following methods:

encrypt_password(self, master_password): Encrypts the password using the master password.
decrypt_password(self, master_password): Decrypts the password using the master password.

### The command.py module has the following function:

add_password(): Prompts the user for a password name, username, and password, creates a new Password object, encrypts the password, and stores it in a file.
view_passwords(): Prompts the user for a master password, reads the password file, decrypts the passwords, and displays them in a user-friendly format.
delete_password(): Prompts the user for a password name, reads the password file, deletes the password if found, and rewrites the password file.

### The encryption.py module has the following function:

encrypt_data(data, key): Encrypts data using a key and returns the encrypted data.
decrypt_data(data, key): Decrypts data using a key and returns the decrypted data.

### The input_validator.py module has the following functionality:

validate_string_input(prompt): Prompts the user for a string and returns it if valid. Handles invalid input by displaying an error message and re-prompting the user.

#### Usage :

 - type in a to add a new password in file .
 - type in v to view all the password in the file you choose.
 - type in d to delete password.
 - type in q to quit the program . 


### The program will display a prompt and wait for the user to enter a command. The available commands are:

a: Add a new password
v: View passwords
d: Delete a password
q: Quit the program

Welcome to the Password Manager!

Enter a command (a/v/d/q): a
Enter app name: Facebook
Enter username: Bakr1
Enter password: mypassword
Enter master key: secret
Password saved successfully!

Enter a command (a/v/d/q): v
Enter master key: secret
Passwords:
- Facebook
  - Username: Bakr1
  - Password: mypassword

Enter a command (a/v/d/q): d
Enter app name: Facebook
Enter master key: secret
Password deleted successfully!

Enter a command (a/v/d/q): v
Enter master key: secret
No passwords found.

Enter a command (a/v/d/q): q
Goodbye!