from colorama import colorama_text
from art import text2art,tprint
import Drinks_page, Donuts_page


tprint("Wellcome to our Coffee-shop")



user_name = str(input("Hi Enter Your Name!: "))

if user_name.isnumeric() or user_name.startswith(" ") or user_name == "":
     raise ValueError("You should enter a character only!")
     
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

    answer = input("\n Drinks(d) Or Donuts(dn)? ")

    if answer.lower() == "d" or answer.lower() == "drinks":
        answer = input("\n Hot Drinks(h) Or Cold Drinks(c)")

        if answer.lower() == "h" or answer.lower() == "hot":
            Drinks_page.hot_drinks()
            answer = input("\n write waht you want of the list: ")
            Drinks_page.take_order("h",answer)

        elif answer.lower() == "c"  or answer.lower() == "cold":
            Drinks_page.cold_drinks()
            answer = input("\n write waht you want of the list: ")
            Drinks_page.take_order("c",answer)

        else:
            print("please check the answer!")
            return process_order()
        

    elif answer.lower() == "dn"  or answer.lower() == "donuts":
        Donuts_page.donuts()
        answer = input("\n write waht you want of the list: ")
        Donuts_page.take_order(answer)

    else:
            print("\n please check the answer!")
            return process_order("y")


    answer = input("\n Do you want add anything else? ")
    return process_order(answer)   


user_answer = "no"
while user_answer == "n" or user_answer == "no":

    input_of_user = input("\n Do you want to order? y(yes) or n(no) ")

    if input_of_user == "y":
                
        process_order(input_of_user)
        Drinks_page.print_your_order()
            #checkout
            #then exit
    else:
        user_answer = input("\n Do you want to exit y(yes) or n(no)? ")

        if user_answer == "y" or user_answer == "yes":
            exit("\n Thank you... see you soon ")
        
            

#while input_of_user != "exit":
#    pass