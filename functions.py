import arabic_reshaper 
from classes import user1

def resh (par1):

    reshaped_text = arabic_reshaper.reshape(par1)
    correct_text = ""
    for i in reshaped_text[::-1]:
        correct_text+= i
    
    return correct_text
def log_in ():
    user_name = input("Enter your name: ")
    x = 0
    while x<1:
        user_password = int(input("Enter your password: "))
        if user_password == user1.get_password():
            print(f"Welcome back {user1.name}") 
            x+=1
        else:
            print("The password is incorrect")        
    return 

def add_progress():
    file = open("my_track.txt","a",encoding="utf-8")
    file.write("\n"+input("What do you want to add?"))
    file.close()
    return

def progress_check():
    file = open("my_track.txt","r",encoding="utf-8")
    cont = file.read()
    print(cont)
    file.close()
    return

def add_absent():
    file = open("absents.txt","a",encoding="utf-8")
    file.write("\n"+input("What do you want to add?"))
    file.close()
    return

def absents_check():
    file = open("absents.txt","r",encoding="utf-8")
    cont = file.read()
    print(cont)
    file.close()
    return