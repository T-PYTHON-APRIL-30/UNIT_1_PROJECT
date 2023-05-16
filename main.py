from functions import *
from classes import *
exit = 0
while exit <1 :
    user_inp = input("do you want to create your account? answer by 'y' for yes and 'n' for no: if you have an account press 'e': ")
    if  user_inp == 'y':
        new =new_user()
        user_inp2 = input(f"Welcome {new.name} do you want to add your progress? 'y' for yes and 'n' for no")
        if user_inp2 == 'y':
            file = open("my_track.txt","a",encoding="utf-8")
            file.write("\n"+input())
            file.close()
        elif user_inp2 == 'n':
            user_inp3 = input("Do you want to see your progress? 'y' for yes and 'n' for no: ")
            if user_inp3 == "y":
                file = open("my_track.txt","r",encoding="utf-8")
                cont = file.read()
                print(cont)
                file.close()
    if user_inp == 'e':
        user_check = input("User name: ")
        pass_check = int(input("Enter your password"))
        if  user_check == user1.name and  user1.get_password() == pass_check :
            print(f"Welcome back {user1.name}")
        """   pass
        if user1.get_password() == pass_check:"""
    elif  user_inp == "n":
        print("Thank you for using the program")
        exit+=1