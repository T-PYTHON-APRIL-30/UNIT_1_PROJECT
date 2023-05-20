import random
class Destination:
    def __init__(self,city,days=1) -> None:
        self.city = city
        self.days = days
        self.attractions = []
        self.restaurants = []
        self.coffee_shops = []
        self.load_data()

    def load_data(self):
        if self.city == "Riyadh":
            self.attractions = ["AlMasmak Fortress", "Souq AlZal", "National Museum of Saudi Arabia","Diriyah","Edge of the World","Camp under the Stars","Ushaiger Heritage Village","The Antiquities Museum"]
            self.restaurants = ["Najd Village Restaurant","Swalief Aldira Restaurant","Alsaudi Restaurant","The Globe Restaurant","Lusin Restaurant","Assaraya Restaurant"]
            self.coffee_shops = ["Camel Step","Sulalat Coffee","Curve Roastery","Mkth Coffee","Knoll Coffee","Atmosphere Coffee","Sohba Coffee"]

        elif self.city == "Jeddah": 
            self.attractions = ["Historic Jeddah", "Jeddah Yacht Club", "Tayebat Museum"]
            self.restaurants = ["Twina Restaurant","Maqadeer Restaurant","Taibat AlHijaz"]
            self.coffee_shops = ["Hemi Cafe and Roastery","CAF Cafe","Medd Cafe & Roastery"]

        elif self.city == "Alula": 
            self.attractions = ["Alaula Tantura", "Harrat Viewpoint", "Aljadidah"]
            self.restaurants = ["Suhail Old Town","Asfar","Harrat"]
            self.coffee_shops = ["Coyard Coffee Roasters","Elephant Rock Cafe By Key","Origin Cafe"]

        elif self.city == "Dammam": 
            self.attractions = ["Ithra Center", "Qarah Mount", "Heritage Village","Dammam Corniche","Half Moon Bay","SCITECH","Alfelwah and Aljowharah Museum","Taybeen Museum"]
            self.restaurants = ["Madina Restaurant","Shwait Alkhalij","Alayyad Abahry","The Pantry Restaurant","The View Restaurant","RBG Grill Restaurant","Asmahan Restaurant","Olio Restaurant"]
            self.coffee_shops = ["llama cafe","UMQ Cafe","ANDES Coffee Roasters","Line Coffee","Andarena Coffee","Hasead Coffee Roasters","White Roastery"]
        
        elif self.city == "AlAhsa": 
            self.attractions = ["AlQarah", "Dougha Handmade Pottery Factory", "Jawatha Mosque","Ibrahim Palace","Souq Al Qaisariya","Uqair Beach","Um Sabah"]
            self.restaurants = ["Dar Albasmah","Lockmat Hasana","Monde Restaurant","Alkeet Restaurant","Salkara Restaurant","Ashas Indian Restaurant","Ninar Restaurant"]
            self.coffee_shops = ["8oz","Barcode Coffee","MO Coffee","EQUAL Coffee Hub","Methods Coffee","BLEND Coffee","Black Swan Coffee","Enigma Coffee"]

        elif self.city == "Taif": 
            self.attractions = ["Mahfouf Restaurant","Shubra Palace Museum", "Al Qahdi Rose Factory", "The Taif Souq","Daka Mountain Park","AlWahba Crater","Hiking in Taif"]
            self.restaurants = ["Boho Restaurant","Ribal Restaurant","Remaj Restaurant","Faraya Restaurant","Mano Restaurant","Mirage Indian Restaurant","Khayal Restaurant","Alsafy Restaurant"]
            self.coffee_shops = ["Tale Coffee","EIHA Coffee","Basma Coffee","Boston Cafe","Port Coffee","Mug Coffee and Roastery","Fandeer Coffee","Coffee Degrees Cafe","Equip Coffee"]
        

    def plan_trip(self):
        itinerary = ""
        for day in range(1, self.days+1):
            itinerary +=f"\nDay {day} in {self.city}:\n"
            itinerary +="-"*30 + "\n"
            attractions = random.sample(self.attractions, k=1)
            restaurants = random.sample(self.restaurants, k=1)
            coffee_shops = random.sample(self.coffee_shops, k=1)
            for attraction in attractions:
                itinerary +="Activity of the day:\n"+"- " + attraction + "\n"
                itinerary += "\n"

            for restaurant in restaurants:
                itinerary +="Restaurant:\n"+"- " + restaurant + "\n"
                itinerary += "\n"

            for coffee in coffee_shops:
                itinerary +="Coffee of the day:\n"+"- " + coffee + "\n"
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




