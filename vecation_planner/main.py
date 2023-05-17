'''
List to-do:
ask for staying days and print suggested plan for each day
Use a Lambda function.
Use at least 1 Class.
Use some form of Error Handling .
Organize Your Code into modules & (or packages)
design a nicer welcomming

'''
def welcoming():
    print("\n")
    print("-"*40)
    print("Welcome to the Visit Saudi Holiday Planner")
    print("-"*40)
    print("We are here to help you plan your holiday based on your preferences\n")



welcoming()

cities=["Riyadh","Jeddah","Alula","Dammam"]
atrractions ={"Riyadh":{"breakfast":"Chapter","activity":"Hiking","lunch":"Full of","coffee shop":"Mkth","dinner":"San Carlo","info":"In the ever-growing and flourishing city of Riyadh, you will discover the birthplace of the Kingdom of Saudi Arabia, along with its historical treasures hidden in the old palaces that witnessed the founding of the kingdom. It is a destination for tourists from all over the globe who wish to discover a world of shopping, entertainment and business. The malls offer the most exciting shopping experience, and the sand dunes combined with the brightest stars in the sky present the most magical experience in nature. It is an environment full of a natural variety and unique characteristics that are intriguing for explorers. On the other side of the bustling city, you can enjoy a variety of experiences in luxurious restaurants that offer their special services, and their elaborate international dishes. Simultaneously, the local Riyadh restaurants will tempt you with their authentic flavors and blend of spices originating from Saudi culture. Everyone is happy in the city of Riyadh where the biggest cultural events are always celebrated. Endless entertainment destinations are always emerging, for the city visitors to have intriguing and renewing experiences."},
              "Jeddah":{"breakfast":"","activity":"","lunch":"","coffee shop":"","dinner":""},
              "Alula":{"breakfast":"","activity":"","lunch":"","coffee shop":"","dinner":""},
              "Dammam":{"breakfast":"","activity":"","lunch":"","coffee shop":"","dinner":""},}
def trend_cities():
    #this function print the cities for user to choose and then print a suggested plan
    print(cities)
    print("\n")
    user_input = input("choose a city: ")
    if user_input in cities:
        print(f"You chose a {user_input}")
        print(f'- Breakfast:{atrractions["Riyadh"]["breakfast"]}\n- Activity of the day:{atrractions["Riyadh"]["activity"]}\n- Lunch:{atrractions["Riyadh"]["lunch"]}\n- Coffee of the day:{atrractions["Riyadh"]["coffee shop"]}\n- Dinner:{atrractions["Riyadh"]["dinner"]}\n')

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

def city_info(city):
    if city in cities:
        print(atrractions["Riyadh"]["info"])
    else:
        print("This city not available yet")
    


choice = 0 
while choice != 4:
    print("1. Trending Destination:")
    print("2. View All Destinations")
    print("3. Search a city")
    print("4. Quit\n")
    choice = int(input("Choose an option: "))

    if choice == 1:
        print("\nTrending Destination: ")
        trend_cities()
    elif choice == 2:
        print("\nAll Destinations:")
        view_all()
        input_city = input("\nChoose a city: ")
        choose_city(input_city)
        city_info(input_city)
        #print information about the choosen city 
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


