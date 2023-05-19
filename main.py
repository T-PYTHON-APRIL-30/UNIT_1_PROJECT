
import flight_class,seats,city,user_class

def main():
      print("welcome to trival booking")

      name= "@"+input("enter your username : ")

      while True:
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
                  if city.is_city(from_city_answer)==False :
                       print("the city not found !! \n##############")
                  elif Passengers_answer.isdigit()==False or int(Passengers_answer)>3 :
                       print("Passengers answer shoud be number less than 3\n############ ")
                  else:
                       flight_class.display_flight_specific(from_city_answer)
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
                            
                       elif flight_no_answer_1=="c":
                            pass
                       else: 
                            raise Exception("err input")               

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
main()