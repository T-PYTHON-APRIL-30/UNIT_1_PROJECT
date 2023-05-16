

def welcoming():
    print("\n")
    print("-"*40)
    print(f"     Welcome to the Visit Saudi Holiday Planner")
    print("-"*40)
    print("We are here to help you plan your holiday based on your preferences\n")



welcoming()

cities=["Riyadh","Jeddah","Alula","Dammam"]
atrractions ={"Riyadh":{"breakfast":"Chapter","activity":"Hiking","lunch":"Full of","coffee shop":"Mkth","dinner":"San Carlo"},
              "Jeddah":{"breakfast":"","activity":"","lunch":"","coffee shop":"","dinner":""},
              "Alula":{"breakfast":"","activity":"","lunch":"","coffee shop":"","dinner":""},
              "Dammam":{"breakfast":"","activity":"","lunch":"","coffee shop":"","dinner":""},}
def trend_cities():
    print(f"Trending Destination:")
    print(cities)
    print("\n")
    user_input = input("choose a city: ")
    if user_input in cities:
        print(f"You chose a {user_input}")
        print(f'Breakfast:{atrractions["Riyadh"]["breakfast"]}\nActivity of the day:{atrractions["Riyadh"]["activity"]}\nLunch:{atrractions["Riyadh"]["lunch"]}\nCoffee of the day:{atrractions["Riyadh"]["coffee shop"]}\nDinner:{atrractions["Riyadh"]["dinner"]}\n')



choice = 0 
while choice != 4:
    print("1. Start plan your holiday")
    print("2. Show the destinations")
    print("3. Search a city")
    print("4. Quit\n")
    choice = int(input("Choose an option: "))

    if choice == 1:
        trend_cities()
    elif choice == 2:
        print("Show the destination")
    elif choice == 3:
        print("searching")

