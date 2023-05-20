from colorama import *
from art import *
import Drinks_page, Donuts_page
from CheckOut_page import checkout_order


tprint("Wellcome to Coffee-shop")



user_name = str(input(Fore.CYAN +"Hi Enter Your Name!: "))

if user_name.isnumeric() or user_name.startswith(" ") or user_name == "":
     raise ValueError(Fore.RED + "You should enter a character only!" + Fore.CYAN)
     
else:
   print(f"\n Wellcome {user_name} \n")
   
print("")


print("in this program you can order some Coffee and Donuts... \n")
print("Look at the list of product \n \n")
print("Coffee")
Drinks_page.hot_drinks() , Drinks_page.cold_drinks() , Donuts_page.donuts()

def process_order(answer:str):

    if answer.lower() == "n" or answer.lower() == "no":
        return answer

    answer = input("\nDrinks(d) Or Donuts(dn)? ")

    if answer.lower() == "d" or answer.lower() == "drinks":
        answer = input("\n Hot Drinks(h) Or Cold Drinks(c): ")

        if answer.lower() == "h" or answer.lower() == "hot":
            Drinks_page.hot_drinks()
            answer = input("\nwrite waht you want of the list: ")
            Drinks_page.take_order("h",answer)

        elif answer.lower() == "c"  or answer.lower() == "cold":
            Drinks_page.cold_drinks()
            answer = input("\nwrite waht you want of the list: ")
            Drinks_page.take_order("c",answer)

        else:
            print(Fore.RED + "please check the answer!" + Fore.CYAN)
            return process_order()
        

    elif answer.lower() == "dn"  or answer.lower() == "donuts":
        Donuts_page.donuts()
        answer = input("\n write waht you want of the list: ")
        Donuts_page.take_order(answer)

    else:
            print(Fore.RED + "\n please check the answer!" + Fore.CYAN)
            return process_order("y")


    answer = input("\nDo you want to add anything else y(Yes) or n(No) ")
    return process_order(answer)   


user_answer = "no"
while user_answer == "n" or user_answer == "no":

    input_of_user = input("\nDo you want to order? y(Yes) or n(No) ")

    if input_of_user.lower() == "y" or input_of_user.lower() == "yes":
                
        process_order(input_of_user)
        Drinks_page.print_your_order()
        
        checkout_order(user_name)

    elif input_of_user.lower() == "n" or input_of_user.lower() == "no":
        user_answer = input("\nDo you want to exit y(Yes) or n(No)? ")

        if user_answer.lower() == "y" or user_answer.lower() == "yes":
            exit("\nThank you... see you soon \n")
        
        elif user_answer.lower() != "n" or user_answer.lower() != "no":
            print(Fore.RED +"\nPlease check the answer?!" + Fore.CYAN)

    else:
        print(Fore.RED + "\nPlease check the answer?!" + Fore.CYAN)

 