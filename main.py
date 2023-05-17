print("welcome to trival booking")

name= "@"+input("enter your username : ")
while True:
    print(f"        hello, {name} \n \
choose by enter the numbers (1 to 6):\n\
1- explore flaghts\n\
2 -find the distance bitween  your city and others cities \n\
3 -check about weather \n\
4- find all your history \n \
5-exit  ")
    answer_menu=input()
    if answer_menu=="1":
        print("")
    elif answer_menu=="2":
        pass
    elif answer_menu=="3":
        pass
    elif answer_menu=="4":
        pass
    elif answer_menu=="5":
        break
    else:
        print("input wrong ! please try again ..")