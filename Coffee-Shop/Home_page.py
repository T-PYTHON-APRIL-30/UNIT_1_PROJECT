from colorama import colorama_text
from art import text2art,tprint
import Drinks_page


wellcome = tprint("Wellcome to our Coffee-shop")
print(wellcome)


user_name = str(input("Hi Enter Your Name!: "))

if user_name.isnumeric() or user_name.startswith(" "):
     raise ValueError("You should enter a charcter only!")
     
else:
   print(f"Wellcome {user_name} \n")
   
print("")

input_of_user = ""


print("in this program you can order some coffee and dounts... \n")
print("Look at the list of product \n \n")
Drinks_page.hot_drinks() , Drinks_page.cold_drinks()


input_of_user = input("Do you want to order? y(yes) or n(no) ")

if input_of_user.lower() == "y" or "yes":
    input_of_user = input("\n Drinks(d) Or Dounts(dn)? ")

    if input_of_user.lower() == "d":
        Drinks_page.hot_drinks()
        input_of_user = input("write waht you want of list: ")
        input_of_user = input_of_user.title()
        Drinks_page.take_order(input_of_user)


    elif input_of_user.lower() == "dn":
        pass
    

#while input_of_user != "exit":
#    pass