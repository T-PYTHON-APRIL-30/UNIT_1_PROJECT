import datetime
import json
class User:
    def __init__(self,user_name:str,tecket_no:str,from_city:str,to_city:str ,seat_no:str,date:str=datetime.datetime.today().date(),Passengers:int=1):
       
        self.user_name=user_name
        self.tecket_no=tecket_no
        self.from_city=from_city
        self.to_city=to_city
        self.date=date
        self.Passengers=Passengers
        self.seat_no=seat_no

    def display(self):
        return f" TECKET NUMBER {self.tecket_no}| you flight :  ({self.from_city}) ==> ({self.to_city}) | \
AT {self.date} PASSENGERS : {self.Passengers} SEAT NUMBER : {self.seat_no} "




    def convert_to_json(self):
        new_user={self.user_name:
                 [{"tecket_no":str(self.tecket_no),
                 "passengers":str(self.Passengers),
                 "from_city":self.from_city,
                 "seat_no":str(self.seat_no),
                 "to_city":self.to_city,
                 "date":str(self.date),}]
                 }
        new_data_4_user={"tecket_no":str(self.tecket_no),
                 "passengers":str(self.Passengers),
                 "from_city":self.from_city,
                 "seat_no":str(self.seat_no),
                 "to_city":self.to_city,
                 "date":str(self.date)}

        with open("user.json") as read:
            obj = json.load(read)
        with open("user.json","w+") as write:

            for key in obj["users"].keys():
                if key==self.user_name:
                    json.dumps(obj["users"][self.user_name].append(new_data_4_user))
                    break
            if self.user_name not in obj["users"]:        
                json.dumps(obj["users"].update(new_user))
            json.dump(obj,write,indent=5)

        read.close()
        write.close()




def find_history_user(user_name:str):

    
    with open("user.json") as read:
        obj = json.load(read)
      

        for i in obj["users"].keys(): #----->for find username
            if i==user_name:
                for j in range(len(obj["users"][user_name])) :#-------->for print data of this username 
                    fill=obj["users"][user_name][j]
                    print(f' TECKET NUMBER {fill["tecket_no"]}| you trip :  ({fill["from_city"]}) ==> ({fill["to_city"]}) | \
AT {fill["date"]} PASSENGERS : {fill["passengers"]} SEAT NUMBER : {fill["seat_no"]}')
            else:
                print("there are no recods")


