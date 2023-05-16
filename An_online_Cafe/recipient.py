from order import Order
from data_menu import coffee_menu


def print_menu():#اخذ الطلب 
    # اطبع المنيو 
    # ارجع الطلب 
    #ممكن ارجع الطلب كسيت عشان احسب التوتال
    # اسوي وايل لوب 
    pass
#اعطيه طلب 
def make_order(order:Order): # 
    order_question= input("would you like to make order, Drinks or foods ")
    if order_question.lower == "yes":
        for i in coffee_menu:
            print("="*10 ,'\n')
                  

make_order()