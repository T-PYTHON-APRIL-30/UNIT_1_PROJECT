from functions import *
x=0
while x<1:
    print (resh("مرحبا بك في برنامجي للعربية اضغط '1' وللخروج اضغط 'خ'"))
    print ("Welcome to my program for english press '2' to exit press 'e'")
    main_user_input = input()
    if main_user_input == '1':
        x=+1
        while x<2:
            print (resh("هل تريد تسجيل الدخول؟ اجب بـ 'ن' لنعم و 'ل' للرفض"))
            user_inp_ar = input()
            if  user_inp_ar == 'ن':
                x+=1
                log_in_ar()

                while True :
                    print(resh('لرؤية خيارات التقدم اضغط "ت" ولرؤية خيارات الغياب اضغط "غ" وللخروج اضغط "خ" : '))
                    user_inp_ar_2 = input()
                    if user_inp_ar_2 == 'ت':
                        progress_options_ar()

                    elif user_inp_ar_2 == 'غ':
                        absents_options_ar()

                    elif user_inp_ar_2 == 'خ':
                        print(resh("شكرا لاستخدامك البرنامج"))
                        break
                    else:
                        print(resh("يرجى التأكد من المدخل لقد ادخلت"))
                        print(user_inp_ar_2)
                        print("\n")

            elif  user_inp_ar == 'ل':
                print(resh("شكرا لاستخدامك البرنامج"))
                break
            else:
                print(resh("يرجى التأكد من المدخل لقد ادخلت"))
                print(user_inp_ar)
                print("\n")

    elif main_user_input == '2':
        x+=1
        while x<2:
            user_inp:str.lower = input("do you want to log-in to your account? answer by 'y' for yes 'n' for no: ")
            if  user_inp == 'y':
                x+=1
                log_in()

                while True :
                    user_inp2:str.lower = input("\nto see progress options press 'p'\nto see absents options 'a'\nto exit press 'e': ")
                    if user_inp2 == 'a':
                        progress_options()

                    elif user_inp2 == 'p':
                        absents_options()

                    elif user_inp2 == 'e':
                        print("Thank you for using the program")
                        break
                    else:
                        print(f"Please check your entery you entered {user_inp2}")

            elif  user_inp == "n":
                print("Thank you for using the program")
                break
            else:
                print(f"Please check your entery you entered {user_inp}")
    elif main_user_input == 'e' or main_user_input == 'خ':
        ar = "شكرا لاستخدامك البرنامج"
        en = "Thank you for using the program"
        print(f'{en} | {resh(ar)}')
        break
    else:
        ar = "يرجى التأكد من المدخل لقد ادخلت"
        en = "please check your entery you entered"
        print(f'{en} |{main_user_input} | {resh(ar)}')
        print("\n")