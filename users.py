class User:
    def __init__(self,name:str,username:str,password:str):
        self.name =name
        self.username=username
        self.passowrd=password
    def print_user(self):
        return f"Hello {self.name}, your username is: {self.username} and your password is: {self.passowrd}"
    def generate_password(self):

        pass

