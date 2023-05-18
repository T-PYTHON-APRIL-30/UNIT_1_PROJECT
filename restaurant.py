# import
from menu import menu

# class menu items
class Item:
    def __init__(self, item, price):
        self.item = item
        self.price = price

    def __str__(self):
        return f"{self.item}: ${self.price:.2f}"

# class order
class Order:
    def __init__(self):
        self.items = []
    
    # add items from the user
    def add_item(self, item):
        self.items.append(item)
    
    # calculate the total
    def calculate_total(self):
        return sum(item.price for item in self.items)

# class restaurant
class Restaurant:
    def __init__(self):
        self.orders = []

    # take order from the user
    def take_order(self):
        order = Order()
        while True:
            print("\nmenu:")
            for item, price in menu.items():
                print(f"{item}: ${price:.2f}")
            choice = input("enter item or exit: ")
            if choice == "exit":
                break
            if choice not in menu:
                print("* item is not on the menu *")
                continue
            item = Item(choice, menu[choice])
            order.add_item(item)
        self.orders.append(order)
        print("* order placed *")
    
    # print all the orders
    def view_orders(self):
        for i, order in enumerate(self.orders):
            print(f"\norder {i+1}:")
            for item in order.items:
                print(item)
            print("total:", f"${order.calculate_total():.2f}")

    # sort menu items by price using lambda function
    def sorted_menu(self):
        print("\nsorted menu by lower prices:")
        sorted_menu = sorted(menu.items(), key = lambda x: x[1])
        for item, price in sorted_menu:
            print(f"{item}: ${price:.2f}")