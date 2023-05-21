from art import *
from colorama import Fore
from stringcolor import *



coffee_list = ['Drinks','Bekery']
menu = filter(lambda i : i.isalpha , coffee_list)
print(tprint("Welcome to the cafe shop",font="cybermedum"))
print(Fore.LIGHTMAGENTA_EX+"we provide",list(menu))


import An_online_Cafe 
from An_online_Cafe import recipient


recipient.print_receipt(recipient.make_order())    


