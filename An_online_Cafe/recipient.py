from order import Order
from data_menu import coffee_menu
from data_menu import bakery_menu

# def print_menu():#اخذ الطلب 
#     if make_order.order
#     print("="*10 ,'\n')

    # اطبع المنيو 
    # ارجع الطلب 
    #ممكن ارجع الطلب كسيت عشان احسب التوتال
    # اسوي وايل لوب 
    #اعطيه طلب 
def make_order():
    while True:
        order_question= input("what wolde you like to order Drinks or bakery: ")
        order=[]  
        if order_question.lower == "d":
            print('-----')
            for key,value in coffee_menu:
                print(f"{key}.................{value}SAR") 
                order_name=input('choose one drink?')
                drinks_quantity=input('how many?')
                drink_order=Order(order_name,coffee_menu[order_name],drinks_quantity)
                order.append(drink_order)
        elif order_question.lower == "bakery":
            for key,value in bakery_menu.items():
                print(f"{key}.................{value}SAR")
                order_name=input('choose one drink?')
                bakery_quantity=input('how many?')
                bakery_order=Order(order_name,bakery_menu[order_name],bakery_quantity) 
                order.append(bakery_order) 
        elif order_question =="exit":
            print("ffffff")
            break

    return order
            
def print_receipt(order):
    if make_order.order_question.lower == "Drinks":
        receipt=make_order.drinks_quantity* coffee_menu.value
    elif make_order.order_question.lower == "bakery":
        receipt=make_order.drinks_quantity* coffee_menu.value
    print(f"The total order is: {receipt}")
    return receipt


make_order()
#print_receipt()    
