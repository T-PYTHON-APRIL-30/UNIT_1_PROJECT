import secrets
import string
from random import shuffle
#from random import choice, shuffle
from art import *
from users import User
from cryptography.fernet import Fernet


def key_generation():
    key = Fernet.generate_key()
    f = Fernet(key)
    print ("key: ",key,"f: ",f)
    return f

def decryption(encrypted_string,key):
    decrypted_string = key.decrypt(encrypted_string)
    return decrypted_string.decode()


def add_passwords(user_details: str):
    file = open("users_passwords.txt", "+a", encoding="utf-8")
    file.write("\n"+str(user_details))
    file.close()

def password_generator(length:int = 8):
    letters = string.ascii_letters
    upper_letters = string.ascii_uppercase
    lower_letters= string.ascii_lowercase
    digits = string.digits
    special_chars = string.punctuation

    #this statment will gurantee that the password will have at least 
    #one upper letter one lower letter one digit and it will only add one
    #special character
    pwd = [secrets.choice(upper_letters),secrets.choice(lower_letters),\
           secrets.choice(digits),secrets.choice(special_chars)]  + \
            [secrets.choice(lower_letters + upper_letters + digits ) for _ in range(length-4)]
    shuffle(pwd)
    pwd = ''.join(pwd)
    return pwd

tprint("Welcome to my password generator",font="bold_script")
tprint("please chose do you want to create a new password or do you want to decrypt the one you have",font="bold_script")
new_old=input("please enter 'new' to create a new password or 'decrypt' to decrypt your password: ")
if new_old=="new":
    length=int(input("please enter the length of the password you need: "))
    while length < 6:
        length=int(input("Please enter a length that is more than 5: "))
elif new_old =="decrypt":
    user_password=input("please enter your encrypted password: ")
    user_key=input("now enter the key to decrypt the password: ")
    print("decrypted password: ",decryption(user_password,user_key))
    


password=password_generator(length)#this function call will generate the password

key=key_generation()#this will generate a key

encrypted_password=key.encrypt(password.encode())# this will encrypt the password using the key

#these statemensts to check if the code is working
print("This is your new password: ",password)
print("encrypted password is: ",encrypted_password)
#print("decrypted password: ",decryption(encrypted_password,key))

#users_list = []
name = input("what is your name: ")
username= input("enter a username: ")
user = User(name,username,password)
user_details=user.print_user()
print(user_details)
add_passwords(user_details)
'''users_list.append(user1)
print(user1)
print(*users_list)'''