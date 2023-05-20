from Drinks_page import price_list, print_your_order
from Employee_page import casher_print
from colorama import *




def checkout_order(name_customer:str):
    sub_total = 0
    total = 0

    for i in price_list:

        sub_total += i

    tax_calculate = lambda sub , tax_amount: sub * tax_amount

    tax = tax_calculate(sub_total, 0.15)

    total = sub_total + tax
    
    print(f"\n INVOICE \n")
    print(f"{casher_print()}\n")
    print(f"Hi {name_customer}\n")
    print(f"{print_your_order()} \n\nSub Total Is {sub_total:.2f} SR \n")
    print(f"TAX Amount: {tax:.2f} SR \n")
    print(f"Total Amount With TAX: {total:.2f} SR \n")

    exit(Fore.WHITE +"Thank you for visiting... :) \n")