
from Store.fruit_file import Fruit_Object
import random
import sys
from Store.Customer import customer



class Store:
    #Customer1 = customer()
    def __init__(self,inventory=None,cart=None):
        self.__inventory = inventory or [Fruit_Object()]
        self.__cart = cart or [Fruit_Object()]
    
    def browse(self):
        list_browse = []
        for Fruit_Object in self.__inventory:
            list_browse.append(str(Fruit_Object))

        for item in list_browse[1:]:
            print(item)
        return str(list_browse[1:])


    

    
    def view_product_info(self,name:str):
        try:
            for Fruit_Object in self.__inventory:
                if str(Fruit_Object.get_name()).lower() == name.lower():
                   founded_product = f"Here's the info on wanted product {str(Fruit_Object.get_name())}, Description: {str(Fruit_Object.get_description())}, Price: {Fruit_Object.get_price()}$"
                   print(founded_product)
                   return  founded_product
            else: 
                print(f"the product with name:{name} is not available right now")
                raise ValueError(f"the product with name:{name} is not available right now")
        except Exception as e:
            return e
    
    
    def search_for_product(self,keyword:str):
        try:
            for Fruit_Object in self.__inventory:
                if str(Fruit_Object.get_name()).lower() == keyword.lower() or str(Fruit_Object.get_description()).lower() == keyword.lower():
                    searched_product = f" Product found and here's its details: {str(Fruit_Object)}"
                    print(searched_product)
                    return searched_product
            else:
                print(f"the product with name:{keyword} is not available right now")
                raise ValueError(f"the product with name:{keyword} is not available right now")
        except Exception as e:
            return e    

    
    def get_recommendations(self):
        try:   
            if not self.__cart:
                print("cart is empty,try adding to the cart first to provide recommendation")
                raise Exception("cart is empty,try adding to the cart first to provide recommendation")
            
            last_purchase = self.__cart[-1].get_name()
            recommended = []
            for Fruit_Object in self.__inventory:
                if str(Fruit_Object.get_name()).lower() != last_purchase:
                    recommended.append(Fruit_Object)
            if not recommended:
                raise Exception("no recommendation available")
            else:
                for Fruit_Object in random.sample(recommended,len(recommended)):
                    recommended_fruit = f"Here's what we recommend: {str(Fruit_Object)}"
                    print(recommended_fruit)
                    return recommended_fruit
        except Exception as e:
            return e
    
    
    def add_product_to_cart(self,item:str):
        try:
            for Fruit_Object in self.__inventory:
                if str(Fruit_Object.get_name()).lower() == item.lower():
                    self.__cart.append(Fruit_Object)
                    added_item = f"{item} has been added to cart"
                    print(added_item)
                    return added_item
                    
            else:
                print(f"{item} not found in inventory")
                raise ValueError(f"{item} not found in the inventory")
        except Exception as e:
            return e
    
    
    def remove_product_from_cart(self,item:str):
        try:
            if not self.__cart:
                print("cart is empty")
                raise Exception("cart is empty")
            else:
                for Fruit_Object in self.__cart:
                    
                    if str(Fruit_Object.get_name()).lower() == item.lower():
                        self.__cart.remove(Fruit_Object)
                        removed_product = f"{item} has been removed"
                        print(removed_product)
                        return removed_product
                else:
                    print(f"{item} not in the cart to remove")
                    raise ValueError(f"{item} not in the cart to remove")
        except Exception as e:
            return e

    
    def list_the_prodcuts(self):
        try:
            if not self.__cart:
                print("cart is empty")
                raise Exception("cart is empty")
            
            else:
                list_of_products_in_cart = f"\n -- \n"
                for Fruit_Object in self.__cart:
                    list_of_products_in_cart += f" here's what in your cart: {Fruit_Object.get_name()}, Price: {Fruit_Object.get_price()}$ \n"
                print(list_of_products_in_cart)
                return list_of_products_in_cart
        except Exception as e:
            return e
    
    
    def checkout(self) -> bool:
        try:
            Customer2 = customer()
            if not self.__cart:
                Customer2.text_to_speech("cart is empty")
                print("cart is empty")
                raise Exception("cart is empty")
        
        
            total_price = sum(Fruit_Object.get_price() for Fruit_Object in self.__cart)
            Customer2.text_to_speech(f"the total price is: {total_price}$")
            print(f"the total price is: {total_price}$")
            Customer2.text_to_speech("enter your city and road respectivley the city is followed by a white space then road:")
            shipping_address_input = input("enter your city and road respectivley the city is followed by a white space then road:")
            if not shipping_address_input.isdigit():
                Customer2.text_to_speech("initiating payment")
                print("initiating payment")
                import time
                time.sleep(2)
                Customer2.text_to_speech("Payment successfull")
                print("Payment successful!")
                Customer2.text_to_speech("Preparing shipment...")
                print("Preparing shipment...")
                time.sleep(2)
                Customer2.text_to_speech(f"shipment to {shipping_address_input} is on ongoing, and here's the receipt")
                print(f"shipment to {shipping_address_input} is on ongoing, and here's the receipt")
                receipt = f"Order Summary: \n --- \n "
                for Fruit_Object in self.__cart[1:]:
                    receipt += f"{Fruit_Object.get_name()}, Price:{Fruit_Object.get_price()}$, "
                receipt += f"\n --- \n Total price:{total_price}$ \n to {shipping_address_input}"
                Customer2.text_to_speech(receipt)
                print(receipt)
                self.__cart = []
            else:
                Customer2.text_to_speech("must be string")
                raise ValueError("must be string")
        except Exception as e:
            return e
    
    def my_dec(func):
        def wrapper(*args,**kwargs):
            Customer3 = customer()
            Customer3.text_to_speech("it shows the status depending on the situation of the order")
            print("it shows the status depending on the situation of the order")
            result = func(*args,**kwargs)
            Customer3.text_to_speech("sorry for any inconvience")
            print("sorry for any inconvenience")
            return result
        return wrapper
    
    
    @my_dec
    def check_delivery_status(self,word):
        Customer4 = customer()
        word1 = ["ongoing","late","postponed"]
        if word.lower() == word1[0].lower():
            Customer4.text_to_speech(word1[0])
            print(word1[0])
        if word.lower() == word1[1].lower():
            Customer4.text_to_speech(word1[1])
            print(word1[1])
        if word.lower() == word1[2].lower():
            Customer4.text_to_speech(word1[2])
            print(word1[2])



    def manager_adding_products_to_inventory(self,Fruit_Object:Fruit_Object):
        self.__inventory.append(Fruit_Object)
    def manager_removing_products_from_inventory(self,WantedFruit_Object:Fruit_Object):
        for Fruit_Object in self.__inventory:
            if Fruit_Object.__name == WantedFruit_Object.__name:
                self.__inventory.remove(Fruit_Object)
                return
            
    def empyting_cart(self):
        self.__cart = []                   


        

    
   
   
   
   
   
   
 