from functions import *
print (resh("مرحبا بك في برنامجي للعربية اضغط '1'"))
print ("Welcome to my program for english press '2'")
main_user_input = input()
if main_user_input == '1':
    print (resh("هل تريد تسجيل الدخول؟ اجب بـ 'ن' لنعم و 'ل' للرفض"))
    user_inp_ar = input()
    if  user_inp_ar == 'ن':
        log_in_ar()

        while True :
            print(resh('لرؤية التقدم اضغط "ت" ولرؤية الغياب اضغط "غ" وللخروج اضغط "خ" : '))
            user_inp_ar_2 = input()
            if user_inp_ar_2 == 'ت':
                progress_options_ar()

            elif user_inp_ar_2 == 'غ':
                absents_options_ar()

            elif user_inp_ar_2 == 'l':
                map = lambda loc: option1() if loc == '0' else (option2() if loc == '1'else "provide a valid index")
                print(map(input("where do you want to go?: ")))

            elif user_inp_ar_2 == 'خ':
                print(resh("شكرا لاستخدامك البرنامج"))
                break

    elif  user_inp_ar == 'ل':
        print(resh("شكرا لاستخدامك البرنامج"))

elif main_user_input == '2':
    

    user_inp:str.lower = input("do you want to log-in to your account? answer by 'y' for yes 'n' for no: ")
    if  user_inp == 'y':
        log_in()

        while True :
            user_inp2:str.lower = input("\nto see progress options press 'p'\nto see absents options 'a'\nto open the location press 'L'\nto exit press 'e': ")
            if user_inp2 == 'a':
                progress_options()

            elif user_inp2 == 'p':
                absents_options()

            elif user_inp2 == 'l':
                map = lambda loc: option1() if loc == '0' else (option2() if loc == '1'else "provide a valid index")
                print(map(input("where do you want to go?: ")))

            elif user_inp2 == 'e':
                print("Thank you for using the program")
                break

    elif  user_inp == "n":
        print("Thank you for using the program")