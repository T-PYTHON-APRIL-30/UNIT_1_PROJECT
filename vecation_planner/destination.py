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
        
        elif self.city == "AlAhsa": 
            self.attractions = ["AlQarah", "Dougha Handmade Pottery Factory", "Jawatha Mosque","Ibrahim Palace","Souq Al Qaisariya","Uqair Beach","Um Sabah"]
            self.restaurants = ["Dar Albasmah"]
            self.coffee_shops = []

        elif self.city == "Taif": 
            self.attractions = ["Shubra Palace Museum", "Al Qahdi Rose Factory", "The Taif Souq","Daka Mountain Park","AlWahba Crater","Hiking in Taif"]
            self.restaurants = []
            self.coffee_shops = []
        

    def plan_trip(self):
        for day in range(1, self.days+1):
            print(f"\nDay {day} in {self.city}:")
            print("-"*30)
            attractions = random.sample(self.attractions, k=1)
            restaurants = random.sample(self.restaurants, k=1)
            coffee_shops = random.sample(self.coffee_shops, k=1)
            print("- Activity of the day:")
            for attraction in attractions:
                print(attraction)
                print("\n")

            print("- Restaurant:")
            for restaurant in restaurants:
                print(restaurant)
                print("\n")

            print("- Coffee of the day:")
            for coffee in coffee_shops:
                print(coffee)
                print("\n")

    def plan_experience(self):
        itinerary = ""
        for day in range(1, self.days+1):
            itinerary +=f"\nDay {day} in {self.city}:\n"
            itinerary +="-"*30 + "\n"
            attractions = random.sample(self.attractions, k=3)
            for attraction in attractions:
                itinerary +="- " + attraction + "\n"
                self.attractions.remove(attraction)
            itinerary += "\n"
        print(itinerary)
        save_file = input("Do you want to save the itinerary to a text file? (Y/N) ")
        if save_file.lower() == "y":
            filename = input("Please enter a filename: ")
            with open(filename, "w") as f:
                f.write(itinerary)
            print(f"Saved itinerary to {filename}.\n")
        else:
            print("Itinerary not saved.\n")
                

        





