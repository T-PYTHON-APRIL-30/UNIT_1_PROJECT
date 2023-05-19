import json


def select_seat(id,row:int,coloum:int):
    
        with open("flight.json")as read:
            obj=json.load(read)
        with open("flight.json","w+") as write:
            seat_list=obj["flights"][id]["seats"]
            seat_choice=seat_list[row][coloum]="▣"
            json.dumps(seat_choice)
            json.dump(obj,write,indent=1)
            read.close()
            write.close()

def seat_confirm(id):
    with open("flight.json")as read:
        obj=json.load(read)
    with open("flight.json","w+") as write:
        seat_list=obj["flights"][id]["seats"]
        for i in range(len(seat_list)):
            for j in range(len(seat_list[0])):
                if seat_list[i][j]=="▣":
                     seat_list[i][j]="▢"
                     json.dumps(seat_list)
        json.dump(obj,write,indent=1)



def seat_reset(id):
    with open("flight.json")as read:
        obj=json.load(read)
    with open("flight.json","w+") as write:
        seat_list=obj["flights"][id]["seats"]
        for i in range(len(seat_list)):
            for j in range(len(seat_list[0])):
                if seat_list[i][j]=="▣":
                     seat_list[i][j]="▆"
                     json.dumps(seat_list)
        json.dump(obj,write,indent=1)
    read.close()
    write.close()
        
def display_seat_choices(id:str):
    with open("flight.json")as read:
        obj=json.load(read)
    seat_list=obj["flights"][id]["seats"]
    print("available seat : ▆ | unavailable seat : ▢ | chosen seat : ▣ \n")
    print("      1   2       3   4  ")
    for i in range(len(seat_list)):
        print(f"{i+1}- ▓ -{seat_list[i][0]}- -{seat_list[i][1]}- | | -{seat_list[i][2]}- -{seat_list[i][3]}- ▓ ")
        print("   ▓         | |         ▓")
    read.close()



"""
select_seat("3000",2,3)
select_seat("3000",2,2)
seat_reset("3000")
select_seat("3000",1,1)
select_seat("3000",3,3)
seat_confirm("3000")

print()





display_seat_choices("3000")"""

def is_confirm_seat(flight_no,row,coloum)->bool:
    with open("flight.json")as read:
        obj=json.load(read)
        seat_list=obj["flights"][id]["seats"]

        if seat_list[row][coloum]=="▣":
            print("the seat already choose !")
            return False
        elif seat_list[row][coloum]=="▢":
            print("you cant take this seat")
            return False
        else:
            return True