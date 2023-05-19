import requests
from geopy.geocoders import Nominatim
from geopy import distance

def show_distanc(city1:str,city2:str):
    locator=Nominatim(user_agent="geoapiExercises")
    l1=locator.geocode(city1)
    l2=locator.geocode(city2)

    loc1=((l1.latitude,l1.longitude))
    loc2=((l2.latitude,l2.longitude))
    return round(distance.distance(loc1,loc2).km)

#print("the distance is : "+show_distanc("abha","jeddah"))

api_key = '30d4741c779ba94c470ca1f63045390a'
def is_city(city):
    weather_data = requests.get(
        f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=imperial&APPID={api_key}")

    if weather_data.json()['cod'] == '404':
        
        return False
    else:
        return True


def fech_wetaher(city):
    weather_data = requests.get(
        f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=imperial&APPID={api_key}")

    weather = weather_data.json()['weather'][0]['main']
    temp = round(weather_data.json()['main']['temp'])
    
    print(f"WEATHER : {weather} | fech_wetaher: {round((temp-32)/1.8)} c")
    


