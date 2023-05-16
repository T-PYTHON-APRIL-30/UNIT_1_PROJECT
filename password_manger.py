"""
name: A string representing the name of the password.
username: A string representing the username associated with the password.
password: A string representing the password.
"""
from encryption import encrypt_data,decrypt_data

class Password:
    def __init__(self,name,username,password):
        self.name=name#name: A string representing the name of the password.
        self.username=username#username: A string representing the username associated with the password.
        self.password=password#password: A string representing the password.

    def encrypt_password(self, master_password):
        """ Encrypts the password using the master password."""
        self.password=encrypt_data(self.password,master_password)


    def decrypt_password(self, master_password):
        """Decrypts the password using the master password."""
        self.password=decrypt_data(self.password,master_password)
        


        
