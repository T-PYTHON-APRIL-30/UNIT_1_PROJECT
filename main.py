from art import *
import my_functions
from colorama import init,Fore,Back,Style
init(autoreset=True)

art1=art("woman",number=10)

print(Fore.LIGHTCYAN_EX+Style.BRIGHT +art1)
tprint("Welcome to my password generator",font="fancy109")
tprint("please chose do you want to create a new password or do you want to decrypt the one you have"
       ,font="fancy109")

import my_menu
my_menu.menu()
#new_user_or_old_user=input("please enter "+Fore.RED+Style.BRIGHT + '"new"'+ Fore.RESET+
#                           " to create a new password or " +Fore.RED+Style.BRIGHT +
#                             '"decrypt"' + Fore.RESET+ " to decrypt your password: ")
'''
if testing_menu.menu()=="1":
   my_functions.new_user()
     
elif new_user_or_old_user =="decrypt":
    my_functions.old_user()
else:
    new_user_or_old_user=input("Plese enter 'new' or 'decrypt': ")'''
    


