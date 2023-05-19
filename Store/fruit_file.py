

class Fruit_Object:
    def __init__(self,name=None,description=None,price=0):
        self.__name = name
        self.__description = description
        self.__price = price

    def get_name(self):
        return self.__name
    def get_description(self):
        return self.__description
    def get_price(self):
        return self.__price
    

    def __str__(self) -> str:
         return f"Fruit Name:{self.__name} it's described as:{self.__description}, Price:{self.__price}$ Dollars"