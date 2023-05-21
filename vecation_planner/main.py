from destination import Destination 

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def welcoming():
    print("\033[1m")  # Bold text
    print("\033[92m")  # Green text
    print(r"""██╗   ██╗██╗███████╗██╗████████╗    ███████╗ █████╗ ██╗   ██╗██████╗ ██╗
██║   ██║██║██╔════╝██║╚══██╔══╝    ██╔════╝██╔══██╗██║   ██║██╔══██╗██║
██║   ██║██║███████╗██║   ██║       ███████╗███████║██║   ██║██║  ██║██║
╚██╗ ██╔╝██║╚════██║██║   ██║       ╚════██║██╔══██║██║   ██║██║  ██║██║
 ╚████╔╝ ██║███████║██║   ██║       ███████║██║  ██║╚██████╔╝██████╔╝██║
  ╚═══╝  ╚═╝╚══════╝╚═╝   ╚═╝       ╚══════╝╚═╝  ╚═╝ ╚═════╝ ╚═════╝ ╚═╝
                                                                        """)
    print("\033[0m")  # Reset text color and style
    print("-" * 73)
    print("\t\tWelcome to the Visit Saudi Trip Planner")
    print("-" * 73)
    print("\nWe are here to help you have the best experince in Saudi Arabia")

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
    if user_input.isdigit():
        print(f"{bcolors.WARNING}Please type a valid city name.\n"+ bcolors.ENDC)
    elif user_input.lower() in [city.lower() for city in cities]:
        matching_city = [city for city in cities if city.lower() == user_input.lower()][0]
        print(f"You chose a {matching_city}")
        while True:
            try:
                days = int(input("How many days you plan to stay? "))
                if days <= 0:
                    raise ValueError(f"{bcolors.WARNING}Please enter a positive integer value for the number of days.\n"+ bcolors.ENDC)
                trip_planner = Destination(matching_city, days)
                trip_planner.plan_trip()
                break
            except ValueError as e:
               print(str(e))
        

def search_city(user_city):

    if user_city.isdigit():
        print(f"{bcolors.WARNING}Please type a valid city name.\n"+ bcolors.ENDC)
    elif user_city.lower() in [city.lower() for city in cities]:
        matching_city = [city for city in cities if city.lower() == user_city.lower()][0]
        print(f"You chose a {matching_city}")
        while True:
            try:
                days = int(input("How many days you plan to stay? "))
                if days <= 0:
                    raise ValueError(f"{bcolors.WARNING}Please enter a positive integer value for the number of days.\n"+ bcolors.ENDC)
                trip_planner = Destination(matching_city, days)
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
                raise ValueError(f"{bcolors.WARNING}Please Choose a Number Between (1-4)\n"+ bcolors.ENDC) 
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


