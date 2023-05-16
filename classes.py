class Users:
    def __init__(self,name:str,password:int):
        self.name = name
        self.__password = password
    
    def get_password (self):
        return self.__password
user1 = Users("aziz",123123)

