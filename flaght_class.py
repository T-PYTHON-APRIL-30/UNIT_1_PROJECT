






seat_list=[
    ["▆","▆","▆","▆"],
    ["▆","▆","▆","▆"],
    ["▆","▆","▆","▆"],
    ["▆","▆","▆","▆"],
]        
#print("▓ -▆- -▆- | | -▆- -▆- ▓ ")

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


select_seat(1,3)
select_seat(1,3)
display_seat_choices()



   
