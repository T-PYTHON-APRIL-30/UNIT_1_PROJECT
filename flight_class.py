import itertools
import json
import datetime
import art
class Flight:
    new_flight_no = itertools.count()
    seat_list=[
    ["▆","▆","▆","▆"],
    ["▆","▆","▆","▆"],
    ["▆","▆","▆","▆"],
    ["▆","▆","▆","▆"],
]

    def __init__(self,from_city:str,to_city:str,date:str=datetime.datetime.today().date(),seats=seat_list):
        
        self.flight_no=next(Flight.new_flight_no)
        self.from_city=from_city
        self.to_city=to_city
        self.date=date
        self.seats=seats

# for convert object of class to json data and send it 
    def confert_to_json(self):
        new_flight_list={str(self.flight_no):{
            "from_city":self.from_city,
            "to_city":self.to_city,
            "date":str(self.date),
            "seats":self.seats

        }}
        with open("flight.json") as read:
            obj = json.load(read)
        with open("flight.json","w+") as write:
                    
            
            json.dumps(obj["flights"].update(new_flight_list))
            json.dump(obj,write,indent=4)


        read.close()
        write.close()

# add new flight
def send_flight(from_city,to_city):
    flight=Flight(from_city,to_city)
    with open("flight.json")as read:
        obj=json.load(read)
        list(obj["flights"])[-1]
        flight.flight_no=int(list(obj["flights"])[-1])+1

    flight.confert_to_json()

def display_flight():
    with open("flight.json")as read:
        obj=json.load(read)
        for key in (obj["flights"]):
            print(f'flight number :{key} ,(({obj["flights"][key]["from_city"]})==>({obj["flights"][key]["to_city"]})) at {obj["flights"][key]["date"]}')

def display_flight_specific(from_city):
    with open("flight.json")as read:
        obj=json.load(read)
        for key in (obj["flights"]):
            if from_city==obj["flights"][key]["from_city"]:
                print(f'flight number :{key} ,(({obj["flights"][key]["from_city"]})==>({obj["flights"][key]["to_city"]})) at {obj["flights"][key]["date"]}')


def get_data_flight(flight_no)-> list:
    new_list=[]

    with open("flight.json")as read:
        obj=json.load(read)

        for key in (obj["flights"]):
            if flight_no==key:
                new_list.append(obj["flights"][key]["date"])
                new_list.append(obj["flights"][key]["to_city"])
        
        return new_list




def tecket(Passengers,from_city:str,to_city:str,name:str,seat:list,date):
     
     print()
     print(f"--------------------------------------------------\n\
NAME : {name[1:].upper()}             PASSENGERS : {Passengers}          \n\
DATE : {date}                             ✈\n\
SEAT NO : {str(seat)[1:-1]} \n\
                          ({from_city.upper()} ➜ {to_city.upper()})\n\
{art.text2art('',font='fancy5',decoration='barcode1')}                            ✈ \n\
--------------------------------------------------\n\n\n\n")
#tecket(2,"abha","riyadh","@khalid",[16],"2023-06-18")





 


   
