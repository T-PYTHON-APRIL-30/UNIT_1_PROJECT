from colorama import *

order_list = list()
price_list = list()

dict_hot_drinks = {"Black Coffee":8, "Latte":10, "Cappuccino":10, "Hot Chocolate":12, "Espresso":7}
dict_cold_drinks = {"Cold Brew":13, "Iced Latte":15, "Iced Coffee with milk":15, "Iced Mocha":15, "Iced Flat White": 15}

name_hot_drinks = list(dict_hot_drinks.keys())
price_hot_drinks = list(dict_hot_drinks.values())

name_cold_drinks = list(dict_cold_drinks.keys())
price_cold_drinks = list(dict_cold_drinks.values())


def hot_drinks():
    count = 1
    print(Fore.WHITE +"\n Hot Drinks"+ Fore.CYAN)

    for i in range(len(name_hot_drinks)):
        print(f"{count}-{name_hot_drinks[i]} {price_hot_drinks[i]}.SR \n")
        count +=1

def cold_drinks():
    count = 1
    print(Fore.WHITE +"\n Cold Drinks" + Fore.CYAN)
    
    for i in range(len(name_cold_drinks)):
        print(f"{count}-{name_cold_drinks[i]} {price_cold_drinks[i]}.SR \n")
        count +=1
        
def take_order(type:str,order:str):
    order = order.title()
    if type.lower() == "h" or type.lower() == "hot": 
        if order in name_hot_drinks:
            order_list.append(order)
            price_list.append(dict_hot_drinks[order])
            print(Fore.WHITE + "\nadded to the invoice" + Fore.CYAN )
            return
        else:
            print( Fore.RED +"please check the name of order" + Fore.CYAN)

    elif type.lower() == "c" or type.lower() == "cold":
        if order in name_cold_drinks:
            order_list.append(order)
            price_list.append(dict_cold_drinks[order])
            print(Fore.WHITE + "\nadded to the invoice" + Fore.CYAN )
            return
        else:
            print(Fore.RED +"please check the name of order" + Fore.CYAN)
    else:
        print(Fore.RED +"Please check the input!"+ Fore.CYAN)
    
        
def print_your_order():
    count = 1
    print(Fore.WHITE+"\nYou added this items " + Fore.CYAN)
    
    for i in range(len(order_list)):
        print(f"{count}-{order_list[i]} {price_list[i]}.SR \n")
        count +=1
    
    return " "
