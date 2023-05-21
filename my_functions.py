from art import *
from users import User
from cryptography.fernet import Fernet
import my_files
import my_password_generator


def key_generation():
    key = Fernet.generate_key()
    #f = Fernet(key)
    #print ("key: ",key,"f: ",f)
    return key

def decryption(encrypted_string,key):
    decrypted_string = key.decrypt(encrypted_string)
    return decrypted_string.decode()


def new_user():
    
    length=int(input("please enter the length of the password you need: "))
    while length < 6:
        length=int(input("Please enter a length that is more than 5: "))
    password=my_password_generator.password_generator(length)#this function call will generate the password
    

    key= key_generation()#this will generate a key
    fernet_key=Fernet(key)
    encrypted_password=fernet_key.encrypt(password.encode())# this will encrypt the password using the key

    #these statemensts to check if the code is working
    #print("This is your new password: ",password)
    #print("encrypted password is: ",encrypted_password)
    #print("decrypted password: ",decryption(encrypted_password,key))

    #users_list = []
    name = input("what is your name: ")
    username= input("enter a username: ")
    user = User(name,username,password)
    user_details=user.print_user()
    encrypted_passwordd=str(encrypted_password)
    keyy=str(key)
    user_keys=f"the key for this username: {username}  is: {str(keyy[2:-1])}"
    user_info=f"Name: {name} username: {username} encrypted password: {encrypted_passwordd[2:-1]}"
    print(user_details)
    my_files.add_passwords(user_info)
    my_files.add_keys(user_keys)
    '''users_list.append(user1)
    print(user1)
    print(*users_list)'''

def old_user():
    user_password=input("please enter your encrypted password: ")
    user_key=input("now enter the key to decrypt the password: ")
    try:
        print("decrypted password: ",decryption(user_password,Fernet(user_key)))
    except:
        print("wrong input")