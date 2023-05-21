import my_functions



string="123dasf"
key=str(my_functions.key_generation())
my_functions.add_keys(string[2:-1])
print ("key type: ",type(key))
print(key)
print(key[2:-1])