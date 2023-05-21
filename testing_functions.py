import secrets
import string
from random import shuffle

def password_generator(length:int = 8):
    #letters = string.ascii_letters
    upper_letters = string.ascii_uppercase
    lower_letters= string.ascii_lowercase
    digits = string.digits
    special_chars = string.punctuation

    #this statment will gurantee that the password will have at least 
    #one upper letter one lower letter one digit and it will only add one
    #special character
    x= [secrets.choice(upper_letters),secrets.choice(lower_letters), secrets.choice(digits),secrets.choice(special_chars)]
    y= [secrets.choice(lower_letters + upper_letters + digits ) for _ in range(length-4)]
    '''pwd = [secrets.choice(upper_letters),secrets.choice(lower_letters),\
           secrets.choice(digits),secrets.choice(special_chars)]  + \
            [secrets.choice(lower_letters + upper_letters + digits ) for _ in range(length-4)]
    '''
    pwd=lambda x,y:x+y
    shuffle(pwd(x,y))
    pwd = ''.join(pwd(x,y))
    return pwd
print(password_generator(10))