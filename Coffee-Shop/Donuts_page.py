from Drinks_page import order_list,price_list
from colorama import *

dict_dounts = {"Glazed":5, "Blueberry":7, "Glazed Chocolate":6, "Long John":6, "Boston Cream":6}

name_donuts = list(dict_dounts.keys())
price_donuts = list(dict_dounts.values())

def donuts():
    count = 1
    print(Fore.WHITE +"\n Donuts" + Fore.CYAN)

    for i in range(len(name_donuts)):
        print(f"{count}-{name_donuts[i]} {price_donuts[i]}.SR \n")
        count +=1

def take_order(order:str):
        order = order.title()
        if order in name_donuts:
            order_list.append(order)
            price_list.append(dict_dounts[order])
            print(Fore.WHITE +"\n added to the invoice" + Fore.CYAN)
            return
        else:
            print(Fore.RED +"\n please check the name of order")
            return take_order(input(Fore.WHITE +"\n write waht you want of the list: " + Fore.CYAN))
