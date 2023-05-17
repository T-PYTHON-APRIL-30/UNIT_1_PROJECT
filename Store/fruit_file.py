
#import sys
#sys.path.append('d:\\PY\\UNIT_1_PROJECT\\Store\\fruit_file.py')
#print(sys.path)
class Fruit_Object:
    def __init__(self,name=None,description=None,price=0):
        self.__name = name
        self.__description = description
        self.__price = price

    def __str__(self) -> str:
         return f"Fruit Name:{self.__name} it's described as:{self.__description}, Price:{self.__price}$"