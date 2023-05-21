from An_online_Cafe import order,data_menu
from art import *


def print_menu(order_question):
    #order_question= input("what wolde you like to order Drinks or Bakery: ")
    if order_question.lower() == "drinks":
        print("="*5 ,"Coffee Mnue☕🍶","="*5,'\n')
        for key,value in data_menu.coffee_menu.items():
            print(f"{key}.................{value}SAR")
        print("="*20,'\n')
    elif order_question.lower() == "bakery":
        print("="*5 ,"🍪🍩Bakert Mnue🥞🥐","="*5,'\n')
        for key,value in data_menu.bakery_menu.items():
            print(f"{key}.................{value}SAR") 
        print("="*20,'\n')


def make_order():
    final_order=[]
    try:        
        while True:
            order_question= input("what would you like to order?")
            if order_question.lower() == "drinks":
                    print_menu(order_question)
                    order_name=input('choose one drink?').lower()
                    drinks_quantity=int(input('how many?'))
                    drink_order=order.Order(order_name,data_menu.coffee_menu[order_name],drinks_quantity)
                    final_order.append(drink_order)
            elif order_question.lower() == "bakery":
                    print_menu(order_question)
                    order_name=input('choose one type of bakery?').lower()
                    bakery_quantity=int(input('how many?'))
                    bakery_order=order.Order(order_name,data_menu.bakery_menu[order_name],bakery_quantity) 
                    final_order.append(bakery_order)
            elif order_question.lower() =="nothing"or"no"or"exit":
                    print("you comlpete your order")
                    break
    except KeyError:
        print("please enter an one of the menu items")
    finally:
        print("thanks! We look forword to see you again at cafe store")
        return final_order
            
def print_receipt(final_order):
    final_total=0
    print(f"your order is\norder name ....... quantity .........price")
    for i in final_order: 
        total=i.quantity*i.price
        print(f" {i.order_name} ........ {i.quantity} ......... {total}")
        final_total+=total
        
    print(f"The total order is: {final_total} SAR")




print_receipt(make_order())    
