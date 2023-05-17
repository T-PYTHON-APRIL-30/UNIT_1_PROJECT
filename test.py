import itertools
import json
class Flaght:
    new_flaght_no = itertools.count()
    def __init__(self,from_city:str,to_city:str):
        
        self.flaght_no=next(Flaght.new_flaght_no)
        self.from_city=from_city
        self.to_city=to_city

    def confert_to_json(self):
        new_flaght_list={str(self.flaght_no):{
            "from_city":self.from_city,
            "to_city":self.to_city
        }}
        with open("flaght.json") as read:
            obj = json.load(read)
        with open("flaght.json","w+") as write:
                    
            
            json.dumps(obj["flaghts"].update(new_flaght_list))
            json.dump(obj,write,indent=5)


        read.close()
        write.close()

        


Flaght1=Flaght("abha","jeddah")
Flaght2=Flaght("abha","jeddah")

Flaght1.confert_to_json()

(print(Flaght1.flaght_no,Flaght2.flaght_no))
seat_list=[
    ["▆","▆","▆","▆"],
    ["▆","▆","▆","▆"],
    ["▆","▆","▆","▆"],
    ["▆","▆","▆","▆"],
]

def select_seat(row:int,coloum:int):
   
    
    if seat_list[row][coloum]=="▣":
        print("the seat already choose !")
    elif seat_list[row][coloum]=="▢":
        print("you cant take this seat")
    else:
        seat_list[row][coloum]="▣"
        return seat_list[row][coloum]

def display_seat_choices():
    for i in range(len(seat_list)):
        print(f"{i+1}- ▓ -{seat_list[i][0]}- -{seat_list[i][1]}- | | -{seat_list[i][2]}- -{seat_list[i][3]}- ▓ ")
        print("   ▓         | |         ▓")


    

        