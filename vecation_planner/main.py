'''
List to-do:
Change README file
design a nicer welcomming

Use some form of Error Handling: DONE
Use a Lambda function: DONE
ask for staying days and print suggested plan for each day: DONE
Use at least 1 Class: DONE
Organize Your Code into modules & (or packages): DONE
'''
from destination import Destination

def welcoming():
    print("\n")
    print("-"*40)
    print("Welcome to the Visit Saudi Holiday Planner")
    print("-"*40)
    print("We are here to help you plan your holiday based on your preferences\n")

welcoming()


cities=["Riyadh","Jeddah","Alula","Dammam","AlAhsa","Taif"]
def trend_cities(cities):
    trend = filter(lambda x:cities.index(x)< 4,cities)
    trend_list =[city for city in trend]
   
    return trend_list

def choose_city():
    for city in cities[4:]:
        print("+ "+city)
    print("\n")
    user_input = input("choose a city: ")
    print("\n")
    if user_input in cities:
        print(f"You chose a {user_input}")
        while True:
            try:
                days = int(input("How many days you plan to stay? "))
                if days <= 0:
                    raise ValueError("Please enter a positive integer value for the number of days.\n")
                trip_planner = Destination(user_input, days)
                trip_planner.plan_trip()
                break
            except ValueError as e:
               print(str(e))
        

def city_info(city):
    for city in cities:
        print("+ "+city)
    print("\n")
    

def search_city(city):
    if city in cities:
        print(f"You chose a {city}")
        while True:
            try:
                days = int(input("How many days you plan to stay? "))
                if days <= 0:
                    raise ValueError("Please enter a positive integer value for the number of days.\n")
                trip_planner = Destination(city, days)
                trip_planner.plan_trip()
                break
            except ValueError as e:
                print(str(e))
    else:
        print(f"This city plans aren't available yet\n")


def city_experience():
    num = 0
    print("\nBest experiences and tours:")
    print("1.Four days in Riyadh")
    print("2.Two days in AlAhsa")
    print("3.Two days in Taif")
    print("4.One day in Jeddah")
    print("\n")
    while True:
        try:
            num = int(input("Choose your experiences: "))
            if num <= 0 or num > 4:
                raise ValueError("Please Choose a Number Between (1-4)\n") 
            if num == 1:
                days = 4
                trip_planner = Destination("Riyadh", days)
                trip_planner.plan_trip()
            elif num == 2:
                trip_planner = Destination("AlAhsa", 2)
                trip_planner.plan_experience()
            elif num == 3:
                trip_planner = Destination("Taif", 2)
                trip_planner.plan_experience()
            elif num == 4:
                trip_planner = Destination("Jeddah", 1)
                trip_planner.plan_trip()
            break
        except ValueError as e:
                print(str(e))     
    


choice = 0 
while choice != 4:
    print("1. Start Plan Your Trip")
    print("2. Best experiences and tours")
    print("3. Search a city")
    print("4. Quit\n")
    choice = int(input("Choose an option: "))

    if choice == 1:
        print("\nTrending Destination: ")
        for trend in trend_cities(cities):
            print("+ "+trend)
        print("\nExplore Destinations: ")
        choose_city()

    elif choice == 2:
        city_experience()
        #print suggested attractions
        #Do you want to add the plan?
        # if yes save it in a txt file
        #if No back
       
    elif choice == 3:
        print("Search a City")
        input_city = input("\nType a saudi city: ")
        search_city(input_city)
     #print information about the choosen city 
        #print suggested attractions or plan
        #Do you want to add the plan?
        # if yes save it in a txt file
        #if No back 


