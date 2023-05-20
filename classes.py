class Users:
    def __init__(self,name:str,password:int):
        self.name = {name:"name"}
        self.__password = {password:"password"}

        return 
    
    def get_password (self):
        return self.__password

user1 = Users("Abdulaziz",123)