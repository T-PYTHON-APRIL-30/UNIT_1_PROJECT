test = "rayan hantoul"
import string
test = test.title()
print(test)


def process_order(answer:str):

    if answer.lower() == "n" or "no":
        return answer

    input_of_user = input("\n Drinks(d) Or Dounts(dn)? ")

    if input_of_user.lower() == "d" or "drinks":
        input_of_user = input("\n Hot Drinks(h) Or Cold Drinks(c)")

        if input_of_user.lower() == "h" or "hot":
            Drinks_page.hot_drinks()
            input_of_user = input("\n write waht you want of the list: ")
            input_of_user = input_of_user.title()
            Drinks_page.take_order("h",input_of_user)

        elif input_of_user.lower() == "c" or "cold":
            Drinks_page.cold_drinks()
            input_of_user = input("\n write waht you want of the list: ")
            input_of_user = input_of_user.title()
            Drinks_page.take_order("c",input_of_user)

        else:
            print("please check the answer!")
            return process_order()

        #elif input_of_user.lower() == "dn" or "dounts":
        #    pass
    answer = input("Do you want add anything else? ")
    process_order(answer)   
       
#
#
#

input_of_user = input("\n Drinks(d) Or Dounts(dn)? ")

        if input_of_user.lower() == "d" or "drinks":
            input_of_user = input("\n Hot Drinks(h) Or Cold Drinks(c)")

            if input_of_user.lower() == "h" or "hot":
                Drinks_page.hot_drinks()
                input_of_user = input("\n write waht you want of the list: ")
                input_of_user = input_of_user.title()
                Drinks_page.take_order("h",input_of_user)

            elif input_of_user.lower() == "c" or "cold":
                Drinks_page.cold_drinks()
                input_of_user = input("\n write waht you want of the list: ")
                input_of_user = input_of_user.title()
                Drinks_page.take_order("c",input_of_user)

            else:
                print("please check the answer!")


        elif input_of_user.lower() == "dn" or "dounts":
            pass
        