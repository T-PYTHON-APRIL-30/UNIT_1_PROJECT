import sys
import random
from Store.Customer import customer
from Store.Market import Store
#from Store.fruit_file import Fruit_Object

def main():

    Customer1 = customer()
    Store_Product1 = Store()
    Store_Product1.browse()

    try:
        while True:
            file = open("Menu.txt", "a+", encoding="UTF-8")
            file.seek(0)
            file.readlines()
            #file.close()
            options = file.readlines()
            options = [options.strip() for option in options]
            break
    
        file.close()
    except Exception as e:
        print(e)
    
main()