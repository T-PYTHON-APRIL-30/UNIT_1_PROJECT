import sys
import random
from Store.Customer import customer
from Store.Market import Store
from Store.fruit_file import Fruit_Object

def main():

    Customer1 = customer()
    Store_Product1 = Store()
    #Customer1.text_to_speech("Please enter your name")
    fruit1 = Fruit_Object("Apple","Green",2)
    fruit3 = Fruit_Object("Blueberry","Blue",1)
    fruit4 = Fruit_Object("Mango","Yellowish",2)
    fruit5 = Fruit_Object("Tomato","Red",4)
    fruit6 = Fruit_Object("Banana","White",2)
    fruit7 = Fruit_Object("Watermellon","Red with green",8)
    fruit8 = Fruit_Object("Rasberry","Red and sweet and sour",2)
    fruit9 = Fruit_Object("Orange","Orange",2)
    fruit10 = Fruit_Object("Coconut","White",5)
    fruit11 = Fruit_Object("Grapes","Tangy",2)
    fruit12 = Fruit_Object("Kiwi","Green and sour",4)
    fruit13 = Fruit_Object("Promegrante","Red with vitamins",3)
    fruit14 = Fruit_Object("Cherry","Red and sweet",1)
    Store_Product1.manager_adding_products_to_inventory(fruit1)
    Store_Product1.manager_adding_products_to_inventory(fruit3)
    Store_Product1.manager_adding_products_to_inventory(fruit4)
    Store_Product1.manager_adding_products_to_inventory(fruit5)
    Store_Product1.manager_adding_products_to_inventory(fruit6)
    Store_Product1.manager_adding_products_to_inventory(fruit7)
    Store_Product1.manager_adding_products_to_inventory(fruit8)
    Store_Product1.manager_adding_products_to_inventory(fruit9)
    Store_Product1.manager_adding_products_to_inventory(fruit10)
    Store_Product1.manager_adding_products_to_inventory(fruit11)
    Store_Product1.manager_adding_products_to_inventory(fruit12)
    Store_Product1.manager_adding_products_to_inventory(fruit13)
    Store_Product1.manager_adding_products_to_inventory(fruit14)
    Store_Product1.empyting_cart()

    try:
            Customer1.text_to_speech("Please enter your name: ")
            name_input = input("Please enter your name: ")
            Customer1.text_to_speech(f"Welcome {name_input} to the store, and here's the options:")
            print(f"Welcome {name_input} to the store, and here's the options")
            menu_file = "Menu.txt"
            with open(menu_file) as f:
                options = f.readlines()
                options = [option.strip() for option in options]
            for option in options:
                print(option)  
            Customer1.text_to_speech_fast(options)
            while True:
            
                Customer1.text_to_speech("Select an option from 1 to 12, 11 for a repeat of the menu: ")
                choice = input("Select an option from 1 to 12, 11 for a repeat of the menu: ")
                if choice == "1":
                    read_prodcuts = str(Store_Product1.browse()) 
                    Customer1.text_to_speech_fast(read_prodcuts)
                elif choice == "2":
                    Customer1.text_to_speech("Enter product name to search: ")
                    name = input("Enter product name to search: ")
                    product_info = Store_Product1.view_product_info(name)
                    Customer1.text_to_speech(product_info)
                    flag = True
                    while flag:
                        Customer1.text_to_speech("would you like to search again? or stop? 1 for searching again 2 for stopping: ")
                        inner_choice = input("would you like to search again? or stop? for searching again 2 for stopping: ")
                        if int(inner_choice) == 1:
                            Customer1.text_to_speech("Enter product name to search: ")
                            name = input("Enter product name to search: ")
                            product_info = Store_Product1.view_product_info(name)
                            Customer1.text_to_speech(product_info)
                        elif int(inner_choice) == 2:
                            Customer1.text_to_speech("searching stopped")
                            print("searching stopped")
                            flag = False
                        elif int(inner_choice) != 1 or int(inner_choice) != 2:
                            Customer1.text_to_speech("please provide 1 or 2")
                            print("pleaae provide 1 or 2")
                    
                elif choice == "3":
                    Customer1.text_to_speech("Enter a search term, either a decscription or name: ")
                    keyword = input("Enter a search keyword, either a decscription or name: ")
                    searched_product = Store_Product1.search_for_product(keyword)
                    Customer1.text_to_speech(searched_product)
                    flag = True
                    while flag:
                        Customer1.text_to_speech("would you like to search again? or stop? 1 for searching again 2 for stopping: ")
                        inner_choice = input("would you like to search again? or stop? for searching again 2 for stopping: ")
                        if int(inner_choice) == 1:
                            Customer1.text_to_speech("Enter a keyword either a description or name to search for a specific product: ")
                            keyword = input("Enter a keyword either a description or name to search for a specific product: ")
                            searched_product = Store_Product1.search_for_product(keyword)
                            Customer1.text_to_speech(searched_product)
                        elif int(inner_choice) == 2:
                            Customer1.text_to_speech("searching stopped")
                            print("searching stopped")
                            flag = False
                        elif int(inner_choice) != 1 or int(inner_choice) != 2:
                            Customer1.text_to_speech("please provide 1 or 2")
                            print("pleaae provide 1 or 2")
                elif choice == "4":
                    reccomendations = Store_Product1.get_recommendations()
                    Customer1.text_to_speech(reccomendations)
                elif choice == "5":
                    Customer1.text_to_speech("Enter a product name to add to cart: ")
                    name = input("Enter a product name to add to cart: ")
                    added_product = Store_Product1.add_product_to_cart(name)
                    Customer1.text_to_speech(added_product)
                    flag = True
                    while flag:
                        Customer1.text_to_speech("would you like to add another item to the cart? or stop? or view you cart? 1 for adding 2 for stopping 3 for viewing the cart: ")
                        inner_choice = input("would you like to add another item to the cart? or stop? 1 for adding 2 for stopping: ")
                        if int(inner_choice) == 1:
                            Customer1.text_to_speech("Enter a product name to add to cart: ")
                            name = input("Enter a product name to add to cart: ")
                            added_product = Store_Product1.add_product_to_cart(name)
                            Customer1.text_to_speech(added_product)
                        elif int(inner_choice) == 2:
                            Customer1.text_to_speech("searching stopped")
                            print("searching stopped")
                            flag = False
                        elif int(inner_choice) == 3:
                            list_prodcuts_in_cart = Store_Product1.list_the_prodcuts()
                            Customer1.text_to_speech(list_prodcuts_in_cart)
                        elif int(inner_choice) != 1 or int(inner_choice) != 2 or int(inner_choice) != 3:
                            Customer1.text_to_speech("please provide 1 or 2 or 3")
                            print("pleaae provide 1 or 2 or 3")
                    
                   
                elif choice == "6":
                    Customer1.text_to_speech("Enter product name to remove from cart: ")
                    name = input("Enter product name to remove from cart: ")
                    removed_product = Store_Product1.remove_product_from_cart(name)
                    Customer1.text_to_speech(removed_product)
                    flag = True
                    while flag:
                        Customer1.text_to_speech("would you like to remove another item to the cart? or stop or view your cart? 1 for adding 2 for stopping 3 for viewing the cart: ")
                        inner_choice = input("would you like to remove another item to the cart? or stop? 1 for adding 2 for stopping: ")
                        if int(inner_choice) == 1:
                            Customer1.text_to_speech("Enter product name to remove from cart: ")
                            name = input("Enter product name to remove from cart: ")
                            removed_product = Store_Product1.remove_product_from_cart(name)
                            Customer1.text_to_speech(removed_product)
                        elif int(inner_choice) == 2:
                            Customer1.text_to_speech("searching stopped")
                            print("searching stopped")
                            flag = False
                        elif int(inner_choice) == 3:
                            list_prodcuts_in_cart = Store_Product1.list_the_prodcuts()
                            Customer1.text_to_speech(list_prodcuts_in_cart)
                        elif int(inner_choice) != 1 or int(inner_choice) != 2 or int(inner_choice) != 3:
                            Customer1.text_to_speech("please provide 1 or 2 or 3")
                            print("pleaae provide 1 or 2 or 3")
                elif choice == "7":
                    list_prodcuts_in_cart = Store_Product1.list_the_prodcuts()
                    Customer1.text_to_speech(list_prodcuts_in_cart)
                elif choice == "8":
                    Store_Product1.empyting_cart()
                    Customer1.text_to_speech("cart emptied")
                elif choice == "9":
                    Store_Product1.checkout()
                elif choice == "10":
                    Customer1.text_to_speech("enter whether you purchased this week or this month, 1 for this week, 2 for this month, 3 for neither: ")
                    choice = input("enter whether you purchased this week or this month, 1 for this week, 2 for this month, 3 for neither: ")
                    try:
                        if int(choice) == 1:
                          Store_Product1.check_delivery_status("ongoing")
                        elif int(choice) == 2:
                         Store_Product1.check_delivery_status("late")
                        elif int(choice) == 3:
                             Store_Product1.check_delivery_status("postponed")
                        elif int(choice) != 1 or int(choice) != 2 or int(choice) != 3:
                            Customer1.text_to_speech("number must be between 1,2,3")
                            raise ValueError("number must be between 1,2,3")
                            
                    except Exception as e:
                        print(e)
                elif choice == "11":
                    Customer1.text_to_speech_fast(options)
                elif choice == "12":
                    Customer1.text_to_speech("Goodbye!")
                    print("Goodbye!")
                    break
                      
    except Exception as e:
        Customer1.text_to_speech(e) 

main()    
                 

    
    
