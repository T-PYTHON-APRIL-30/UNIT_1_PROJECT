from functions import *

user_inp:str.lower = input("do you want to log-in to your account? answer by 'y' for yes 'n' for no: ")
if  user_inp == 'y':
    log_in()
    exit = 0
    while exit <1 :
        user_inp2:str.lower = input("\nto add to your lab progress press 'a'\nto see your lab progress press 'p'\nto open other options press 'o'\nto exit press 'e': ")
        if user_inp2 == 'a':
            add_progress()

        elif user_inp2 == 'p':
            progress_check()

        elif user_inp2 == 'o':
            user_inp3:str.lower = input("\n\nto add to your absents press 'a'\nto see your absents press 'p'\nto exite press 'e': ")
            if user_inp3 == 'a':
                add_absent()

            elif user_inp3 == 'p':
                absents_check()

            elif user_inp3 == 'e':
                print("Thank you for using the program")
                exit+=1
        
        elif user_inp2 == 'e':
            print("Thank you for using the program")
            exit+=1

elif  user_inp == "n":
    print("Thank you for using the program")