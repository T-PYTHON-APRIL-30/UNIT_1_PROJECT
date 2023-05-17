
from Store.fruit_file import Fruit_Object
import random
import sys
#sys.path.append('d:\\PY\\UNIT_1_PROJECT\\Store\\Market.py')


class Store:
    def __init__(self,inventory=None,cart=None):
        self.__inventory = inventory or [Fruit_Object()]
        self.__cart = cart or [Fruit_Object()]
    
    def browse(self):
        #for Fruit_Object in self.__inventory:
            #print(Fruit_Object)
        print("working")

    
    def view_product_info(self,name):
        try:
            for Fruit_Object in self.__inventory:
                if Fruit_Object.__name.lower() == name.lower():
                    print(Fruit_Object)
            else: 
                raise ValueError(f"the product with name:{name} is not avaiable right now")
        except Exception as e:
            print(e)
    
    
    def search_for_product(self,keyword):
        try:
            for Fruit_Object in self.__inventory:
                if Fruit_Object.__name == keyword or Fruit_Object.__description == keyword:
                    print(f"item found an here's it's details: {Fruit_Object}")
            else:
                raise ValueError(f"the product with name:{keyword} is not avaiable right now")
        except Exception as e:
            print(e)    

    
    def get_recommendations(self):
        if not self.__cart:
            print("cart is empty,try adding to the cart first to provide recommendation")
            return
        last_purchase = self.__cart[-1].__name
        recommended = []
        for Fruit_Object in self.__inventory:
            if Fruit_Object.__name != last_purchase:
                recommended.append(Fruit_Object)
        if not recommended:
            print("no recommendations available")
        else:
            print("you might also like")
            for Fruit_Object in random.sample(recommended,min(len(recommended)),3):
                print(Fruit_Object)
    
    
    def add_product_to_cart(self,item):
        try:
            for Fruit_Object in self.__inventory:
                if Fruit_Object.__name.lower() == item.lower():
                    self.__cart.append(item)
                    print(f"{item} has been added to cart")
                    return
            else:
                raise ValueError(f"{item} not found in the inventory")
        except Exception as e:
            print(e)
    
    
    def remove_product_from_cart(self,item):
        try:
            if not self.__cart:
                print("nothing in the cart to remove")
                return
            else:
                for Fruit_Object in self.__cart:
                    if Fruit_Object.__name.lower() == item.lower():
                        self.__cart.remove(Fruit_Object)
                        print(f"{item} has been removed")
                        return
                else:
                    raise ValueError(f"{item} no in the cart to remove")
        except Exception as e:
            print(e)

    
    def list_the_prodcuts(self):
        if not self.__cart:
            print("cart is empty")
            return
        else:
            print("the items in the cart:")
            for Fruit_Object in self.__cart:
                 print(Fruit_Object)
    
    
    def checkout(self) -> bool:
        if not self.__cart:
            print("cart is empty")
            return False
        
        total_price = sum(Fruit_Object.__price for Fruit_Object in self.__cart)
        print(f"the total price is: {total_price}$")
        try:
            shipping_address_input = input("enter your city and road respectivley:")
            print("payment success")
            import time
            time.sleep(2)
            print("Payment successful!")
            print("Preparing shipment...")
            time.sleep(2)
            print(f"shipment to {shipping_address_input} is on ongoing, and here's the receipt")
            receipt = f"Order Summary:\n ------- \n"
            for Fruit_Object in self.__cart:
                receipt += f"{Fruit_Object.__name}, Price:{Fruit_Object.__price}"
            receipt += f"\n --- \n Total price:{total_price}$\n to {shipping_address_input}"
            print(receipt)
            self.__cart = []
        except Exception as e:
            print(e)
    
    
    def manager_adding_products_to_inventory(self,Fruit_Object:Fruit_Object):
        self.__inventory = Fruit_Object
    def manager_removing_products_from_inventory(self,WantedFruit_Object:Fruit_Object):
        for Fruit_Object in self.__inventory:
            if Fruit_Object.__name == WantedFruit_Object.__name:
                self.__inventory.remove(Fruit_Object)
                return

    
    def my_dec(func):
        def wrapper():
            print("it shows thr status depending on the situation of the order")
            result = func()
            print("sorry for any inconvience")
            return result
        return wrapper
    
    
    @my_dec
    def check_delivery_status(self,word):
        word1 = ["ongoing","late","postponed"]
        if word.lower() == word1[0].lower():
            print(word1[0])
        if word.lower() == word1[1].lower():
            print(word1[1])
        if word.lower() == word1[2].lower():
            print(word1[2])


                      


        

    
   
   
   
   
   
   
 