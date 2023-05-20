
import flight_class,seats,city,user_class

def main():
      print("welcome to trival booking")

      name= "@"+input("enter your username : ")

      while True:
          if name=="@admin":
            adimin_from_city_anwser=input("your origin city : ")
            adimin_to_city_anwser=input("destination city : ")
            if city.is_city(adimin_from_city_anwser)==False and city.is_city(adimin_to_city_anwser)==False :
                  raise Exception("the city not found")
            else:
                  anwser_y_n_date=input("do you want the flight today ? (y/n) : ")
                  if anwser_y_n_date=="y":
                        flight_class.send_flight(adimin_from_city_anwser,adimin_to_city_anwser)
                        print("the flight add successfully !")
          else:
            print()
            print(f"hello, {name} \n \
1 -->  explore your flight\n\
2 -->  explore all flights\n\
3 --> find the distance bitween your city and others cities \n\
4 --> check about weather \n\
5 --> find all your history \n \
6 --> exit  ")
            answer_menu=input("choose by enter the numbers (1 to 6): ")
            if answer_menu=="1":

                    from_city_answer=input("your origin city : ")
                    Passengers_answer=input("how many Passengers with you : ")
                    print()
                    if city.is_city(from_city_answer)==False :
                         print("the city not found !! \n##############")
                    elif Passengers_answer.isdigit()==False or int(Passengers_answer)>3 :
                         print("Passengers answer shoud be number less than 3\n############ ")
                    else:
                         flight_class.display_flight_specific(from_city_answer)
                         print()
                         flight_no_answer_1=input("choose the flight by writing the the flight number (if your destination city not here create new one by writing 'c'): ")
                         if flight_no_answer_1.isdigit():
                              seats.display_seat_choices(flight_no_answer_1)
                              new_list_add_passenger=[]
                              for i in range(int(Passengers_answer)):
                                seat_choice_answer=input("choose seat by writing row frist then coloum (e.g row: 1 coloum: 3 -->13): ")
                                if int(seat_choice_answer[0])<=4 and int(seat_choice_answer[1])<=4 and int(seat_choice_answer[0])>=1 and int(seat_choice_answer[1])>=1:                                   
                                      seats.select_seat(flight_no_answer_1,int(seat_choice_answer[0])-1,int(seat_choice_answer[1])-1)
                                      seats.display_seat_choices(flight_no_answer_1)
                                      new_list_add_passenger.append(seat_choice_answer)
                                else:
                                     seats.seat_reset(flight_no_answer_1)
                                     raise Exception("out of index !")

                              data=flight_class.get_data_flight(flight_no_answer_1)

                              price=lambda distance:round(int(distance)*0.7*int(Passengers_answer))
                              print(F"\nthe price : {price(city.show_distanc(from_city_answer,data[1]))} SAR ")

                              confirm_answer=input("do you want to confirm ? (y/n) : ")
                              if confirm_answer=="n":
                                   seats.seat_reset(flight_no_answer_1)
                              elif confirm_answer=="y":
                                   seats.seat_confirm(flight_no_answer_1)
                                   add_to_user=user_class.User(name,flight_no_answer_1+seat_choice_answer,from_city_answer,data[1],str(new_list_add_passenger)[1:-1],Passengers_answer,data[0])
                                   add_to_user.convert_to_json()
                                   flight_class.tecket(Passengers_answer,from_city_answer,data[1],name,str(new_list_add_passenger)[1:-1],data[0])
                                   add_to_user.display()
                                   input("")
                              else:
                                   raise Exception("err input")     

                         elif flight_no_answer_1=="c":
                              to_city_anwser=input("destination city : ")
                              if city.is_city(from_city_answer)==False :
                                   raise Exception("the city not found")
                              else:
                                   anwser_y_n_date=input("do you want the flight today ? (y/n) : ")
                                   if anwser_y_n_date=="y":
                                        flight_class.send_flight(from_city_answer,to_city_anwser)
                                        print("the flight add successfully !")
                                        input('')
                                   elif anwser_y_n_date=="n":
                                        date_answer=input("write the date of flight : ")
                                        flight_class.send_flight(from_city_answer,to_city_anwser,date_answer)
                                        print("the flight add successfully !")
                                        input('')
                                   else:
                                        raise Exception("err input") 

      
                         else: 
                              raise Exception("err input")               

            elif answer_menu=="2":
                flight_class.display_flight()
                input()
            elif answer_menu=="3":
                frist_city_answer=input("frist city : ")
                second_city_answer=input("second city : ")
                if city.is_city(frist_city_answer)==False and second_city_answer:
                     print("the city not found !! \n##############")
                else:
                     price =lambda distance : round(distance*0.6*1)
                     print(f"the distance bitween {frist_city_answer} and {second_city_answer}is : {city.show_distanc(frist_city_answer,second_city_answer)} \n the duration : {city.calculate_duration(city.show_distanc(frist_city_answer,second_city_answer))}\n the Expected price : {price(city.show_distanc(frist_city_answer,second_city_answer))} SAR")
                     input('')

            elif answer_menu=="4":
                 city_answer=input("write the city name")
                 if city.is_city(city_answer)==False:
                      print(f"{city_answer} not found !")
                 else:
                      city.fech_wetaher(city_answer)
                      input()
            elif answer_menu=="5":
                 user_class.find_history_user(name)
                 input()
            elif answer_menu=="6":
                break
            else:
                print("input wrong ! please try again ..")
main()