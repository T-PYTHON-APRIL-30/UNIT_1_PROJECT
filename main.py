from SearchPhone import Checkphone
from SocialTracker import TwitterChecker, microsoft_checker
from art import *
from termcolor import colored

def print_text_art(text, font, color):
    text_art = text2art(text, font)
    colored_text_art = colored(text_art, color)
    print(colored_text_art)

print_text_art("PhoneChecker ", "block", 'red')


choose= int(input("please choose 1 if you want search a single number ,, or  2 if you want upload multi number: -"))
if choose == 1:
    Singlphone=(input("Please Provide a Phone Number :- "))
    userinput=Checkphone(Singlphone.split())
    print(f"Phone Number is : {Singlphone}\n")
    userinput.search_name()
    userinput.search_facebook()
    TwitterChecker.search_twitter(Singlphone)
    microsoft_checker.Microsofot_checker(Singlphone[3:])
elif choose == 2:
    phone_checker = open('phone.txt','r+',encoding='utf-8')
    for line in phone_checker:
        print(f"Phone Number is : {line.split()}\n")
        face =Checkphone(line.split())
        face.search_name()
        face.search_facebook()
        TwitterChecker.search_twitter(line.split())
        microsoft_checker.Microsofot_checker(line[3:])
        print("---"*5)

else:
    exit()
