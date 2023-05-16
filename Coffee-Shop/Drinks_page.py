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
    print("Hot Drinks")

    for i in range(len(name_hot_drinks)):
        print(f"{count}-{name_hot_drinks[i]} {price_hot_drinks[i]}.SR \n")
        count +=1

def cold_drinks():
    count = 1
    print("Cold Drinks")
    
    for i in range(len(name_cold_drinks)):
        print(f"{count}-{name_cold_drinks[i]} {price_cold_drinks[i]}.SR \n")
        count +=1
        
def take_order(order):
    if order in name_hot_drinks:
        order_list.append(order)
        price_list.append(dict_hot_drinks[order])
        print("added to the invoice")
        return
    elif order in name_cold_drinks:
        order_list.append(order)
        price_list.append(dict_cold_drinks[order])
        print("added to the invoice")
        return
        
    else:
        print("please check the name of order")

