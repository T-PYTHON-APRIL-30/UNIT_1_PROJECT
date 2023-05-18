'''
List to-do:
Use a Lambda function.
Use some form of Error Handling .
design a nicer welcomming

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

cities=["Riyadh","Jeddah","Alula","Dammam"]
atrractions ={"Riyadh":{"breakfast":"Chapter","activity":"Hiking","lunch":"Full of","coffee shop":"Mkth","dinner":"San Carlo","info":""},
              "Jeddah":{"breakfast":"","activity":"","lunch":"","coffee shop":"","dinner":""},
              "Alula":{"breakfast":"","activity":"","lunch":"","coffee shop":"","dinner":""},
              "Dammam":{"breakfast":"","activity":"","lunch":"","coffee shop":"","dinner":""},}
def trend_cities():
    #this function print the cities for user to choose and then print a suggested plan
    for city in cities:
        print("+ "+city)
    print("\n")
    user_input = input("choose a city: ")
    print("\n")
    if user_input in cities:
        print(f"You chose a {user_input}")
        days = int(input("How many days you plan to stay? "))
        trip_planner = Destination(user_input, days)
        trip_planner.plan_trip()
        

def view_all():
    for city in cities:
        print("+ "+city)
    print("\n")

def choose_city(city):
    if city in cities:
        print(f"Here a suggested plan for {city}:")
        print(f'- Breakfast:{atrractions["Riyadh"]["breakfast"]}\n- Activity of the day:{atrractions["Riyadh"]["activity"]}\n- Lunch:{atrractions["Riyadh"]["lunch"]}\n- Coffee of the day:{atrractions["Riyadh"]["coffee shop"]}\n- Dinner:{atrractions["Riyadh"]["dinner"]}\n')
    

def search_city(city):
    if city in cities:
        print(f"{city} plans\n")
    else:
        print(f"This city not available yet\n")

'''def city_info(city):
    if city in cities:
        print(atrractions["Riyadh"]["info"])
    else:
        print("This city not available yet")'''

def exper_city():
    num = 0
    print("\nBest experiences and tours:")
    print("1.Four days in Riyadh")
    print("2.Two days in AlAhsa")
    print("3.Two days in Taif")
    print("4.One day in Jeddah")
    print("\n")
    num = int(input("Choose your experiences:"))
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
    


choice = 0 
while choice != 4:
    print("1. Start Plan Your Trip")
    print("2. Best experiences and tours")
    print("3. Search a city")
    print("4. Quit\n")
    choice = int(input("Choose an option: "))

    if choice == 1:
        print("\nTrending Destination: ")
        trend_cities()

    elif choice == 2:
        exper_city()
        #print suggested attractions
        #Do you want to add the plan?
        # if yes save it in a txt file
        #if No break
       
    elif choice == 3:
        print("search")
        input_city = input("\nType a saudi city: ")
        search_city(input_city)
     #print information about the choosen city 
        #print suggested attractions or plan
        #Do you want to add the plan?
        # if yes save it in a txt file
        #if No break


