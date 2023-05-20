from SearchPhone import Checkphone
from art import *
from termcolor import colored

#ascii style

def print_text_art(text, font, color):
    text_art = text2art(text, font='small')
    colored_text_art = colored(text_art, color)
    print(colored_text_art)

print_text_art("PhoneXChecker ", "starwars", 'red')

#User InterFace
print("Please select an option:\n")
print("1. Search for a specific phone number.")
print("2. Search for multiple phone numbers.")
option = int(input("Enter your option (1 or 2): \n"))
try:

    if option == 1:
        Singlphone=(input("Enter the phone number:-  "))
        userinput=Checkphone(Singlphone.split())
        userinput1 = Checkphone(Singlphone[3:])
        print(f"Phone Number is : {Singlphone}\n")
        print("\n")
        execute = [userinput.name_checker, userinput.twitter_checker, userinput.facebook_checker, userinput1.microsoft_checker]
        execute_script = lambda func: func()
        list(map(execute_script, execute))



    elif option == 2:
        phone_checker = open('phone.txt','r+',encoding='utf-8')
        for line in phone_checker:
            print(f"Phone Number is : {line}\n")
            multi =Checkphone(line.split())
            cut_num = Checkphone(line[3:])
            execute= [multi.name_checker(),multi.twitter_checker(),multi.facebook_checker(),cut_num.microsoft_checker()]
            print("---"*5)

    else:
        exit()
except Exception as e:
    print(f"An error occurred: {e}")
