import arabic_reshaper 
from classes import Users

def resh (par1):

    reshaped_text = arabic_reshaper.reshape(par1)
    correct_text = ""
    for i in reshaped_text[::-1]:
        correct_text+= i
    
    return correct_text
x= 0
def new_user ():
    new_user_name = input("Enter your name: ")
    x = 0
    while x<1:
        new_user_password = int(input("Enter your password: "))
        password_check = str(new_user_password)
        if len(password_check) <8:
            print("please enter at least 8 numbers ") 
        else:
            x+=1
            new = Users(new_user_name,new_user_password)
            print (f"Your username is: {new_user_name}\nYour password is {new_user_password}")
    return new

'''

user_count_open.close()

user_count = user_count.read
def users():
    user_count_open = open("user_count.txt","w+",encoding="utf-8"
    user_count_read = user_count_open.read()
    
    user_str = str(user_count)
    user1= ("User")
    user1 += user_str

    user1 = Users(input("Enter your name"),input("Enter your password"))
    return user1
'''

