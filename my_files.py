def add_passwords(user_details: str):
    file = open("users_passwords.txt", "+a", encoding="utf-8")
    file.write("\n"+str(user_details))
    file.close()

def add_keys(user_keys: str):
    file = open("users_keys.txt", "+a", encoding="utf-8")
    file.write("\n"+str(user_keys))
    file.close()

def Display_passwords():
        file = open("users_passwords.txt", "r", encoding="utf-8")
        content=file.read()
        print(content)
        file.close()

def Display_keys():
        file = open("users_keys.txt", "r", encoding="utf-8")
        content=file.read()
        print(content)
        file.close()

#userinput="khalid"
def show_passwords(user_input):
    with open("users_passwords.txt", "r") as target:
        for line in target:
            if user_input in line:
                print(line)#101

def show_keys(user_input):
    with open("users_keys.txt", "r") as target:
        for line in target:
            if user_input in line:
                print(line[-45:])