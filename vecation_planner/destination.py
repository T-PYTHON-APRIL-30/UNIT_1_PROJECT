import random
class Destination:
    def __init__(self,city,days) -> None:
        self.city = city
        self.days = days
        self.attractions = []
        self.restaurants = []
        self.coffee_shops = []
        self.load_data()

    def load_data(self):
        if self.city == "Riyadh":
            self.attractions = ["AlMasmak Fortress", "Souq AlZal", "National Museum of Saudi Arabia"]
            self.restaurants = ["Najd Village Restaurant","Swalief Aldira Restaurant","Alsaudi Restaurant"]
            self.coffee_shops = ["Camel Step","Sulalat Coffee","Curve Roastery"]

        elif self.city == "Jeddah": 
            self.attractions = ["Historic Jeddah", "Jeddah Yacht Club", "Tayebat Museum"]
            self.restaurants = ["Twina Restaurant","Maqadeer Restaurant","Taibat AlHijaz"]
            self.coffee_shops = ["Hemi Cafe and Roastery","CAF Cafe","Medd Cafe & Roastery"]

        elif self.city == "Alula": 
            self.attractions = ["Alaula Tantura", "Harrat Viewpoint", "Aljadidah"]
            self.restaurants = ["Suhail Old Town","Asfar","Harrat"]
            self.coffee_shops = ["Coyard Coffee Roasters","Elephant Rock Cafe By Key","Origin Cafe"]

        elif self.city == "Dammam": 
            self.attractions = ["Ithra Center", "Qarah Mount", "Heritage Village"]
            self.restaurants = ["Madina Restaurant","Shwait Alkhalij","Alayyad Abahry"]
            self.coffee_shops = ["llama cafe","UMQ Cafe","ANDES Coffee Roasters"]

    def plan_trip(self):
        for day in range(1, self.days+1):
            print(f"\nDay {day} in {self.city}:")
            print("-"*30)
            attractions = random.sample(self.attractions, k=1)
            restaurants = random.sample(self.restaurants, k=1)
            coffee_shops = random.sample(self.coffee_shops, k=1)
            print("Activity of the day:")
            for attraction in attractions:
                print(attraction)
                print("\n")

            print("Restaurant:")
            for restaurant in restaurants:
                print(restaurant)
                print("\n")

            print("Coffee of the day:")
            for coffee in coffee_shops:
                print(coffee)
                print("\n")


days = int(input("How many days you plan to stay? "))
trip_planner = Destination("Riyadh", days)
trip_planner.plan_trip()


