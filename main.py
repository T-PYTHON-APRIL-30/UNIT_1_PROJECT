import sys
import random
from Store.Customer import customer
from Store.Market import Store

def main():

    Customer1 = customer()
    Store_Product1 = Store()
    

    try:
        while True:
            file = open("Menu.txt", "a+", encoding="UTF-8")
            file.seek(0)
            file.readlines()
            file.close()
            break
    

    except Exception as e:
        print(e)