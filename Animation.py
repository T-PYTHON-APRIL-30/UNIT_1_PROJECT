from playsound import playsound
from stringcolor import * 
playsound('sounds/WelcomeSpeaceToon.mp3')

print(cs("🎊🎊😍 This Is a Program For Animations 😍🎊🎊 ","orchid" ))


#Parent Class
class Anime:
    def __init__(self, animeName:str,anemeclassification:str,anieRating:float,showtime:int) -> None:
        self.animeName = animeName
        self.anemeclassification=anemeclassification
        self.anieRating=anieRating
        self.showtime=showtime

    def anime_informations(self,animeName,anemeclassification,anieRating,showtime):
        return f"Anime name is {animeName}, Classification is {anemeclassification}, rating is {anieRating}, and showtime of anime is {showtime}"
#Sub Classes
class action(Anime):
    def __init__(self, animeName: str, anemeclassification: str, anieRating: float, showtime: int) -> None:
        super().__init__(animeName, anemeclassification, anieRating, showtime)

    def anime_informations(self, animeName, anemeclassification, anieRating, showtime):
        return super().anime_informations(animeName, anemeclassification, anieRating, showtime)
    
class comedy(Anime):
    def __init__(self, animeName: str, anemeclassification: str, anieRating: float, showtime: int) -> None:
        super().__init__(animeName, anemeclassification, anieRating, showtime)

    def anime_informations(self, animeName, anemeclassification, anieRating, showtime):
        return super().anime_informations(animeName, anemeclassification, anieRating, showtime)
    
class drama(Anime):
    def __init__(self, animeName: str, anemeclassification: str, anieRating: float, showtime: int) -> None:
        super().__init__(animeName, anemeclassification, anieRating, showtime)

    def anime_informations(self, animeName, anemeclassification, anieRating, showtime):
        return super().anime_informations(animeName, anemeclassification, anieRating, showtime)



while True:
    answer = input(underline("Do you want to stay in the program or leave ❓ (( Press 'S' to stay and 'E' to exitt)) ❗️ "))
    if answer.lower() == 's':
         pass
    elif answer.lower() == 'e':
         break
    else:
        raise f"enter s or e"
    Ratings = int(input("Do you prefer action🎬 or comedy 🥳 or drama🔮 ❓ (( Press 1 for the ACTION, 2 for COMEDY, 3 for DRAMA ))❓"))
    if Ratings == 1:
        newlistname =  ["Conan","digitalis jungle","Gundam Wings"]
        filtered_list = list(filter(lambda element: element < element[3], newlistname ))
        print("the filtered list is :")
        print(f"-{filtered_list}")
        song = input(cs("Do you want to hear a song 🎼 ❓ (( Press 'Y' if you agree and 'N' if you refuse )) 🎤","#ffff87"))
        if song.lower() == 'y':
            choose = int(input(" 🎇🎇 Which anime song do you want to hear ❓ (( Press '1' for CONAN '2' for DIGITALS JUNGLE '3' for GUNDAM WINGS)) ❗️  🎇🎇"))
            if choose == 1:
                playsound('sounds/conan.mp3')
                continue
            elif choose == 2:
                playsound('sounds/digital.mp3')
            elif choose == 3:
                playsound('sounds/gandam.mp3')
            else:
                raise f"enter number 1 or 2 or 3"
        elif song.lower() == 'n':  
            answer = input(underline("Do you want to stay in the program or leave ❓ (( Press 'S' to stay and 'E' to exitt)) ❗️ "))
            if answer.lower() == 's':
                pass
            elif answer.lower() == 'e':
                break
        else:
            raise f" You must ansower y or n"
    elif Ratings == 2:
        newlistname = ["Kudo and Modo","Moca","police Academy"]
        print(f"- {newlistname}")
        song = input(cs("Do you want to hear a song🎼 ❓ (( Press 'Y' if you agree and 'N' if you refuse )) 🎤","#ffff87"))
        if song.lower() == 'y':
            choose = int(input("  🎇🎇 Which anime song do you want to hear ❓ (( Press '1' for Kudo and Modo '2' for Moca '3' for police Academy)) ❗️ 🎇🎇"))
            if choose == 1:
                playsound('sounds/codo.mp3')
            elif choose == 2:
                playsound('sounds/moca.mp3')
            elif choose == 3:
                playsound('sounds/acadimy.mp3')
            else:
                raise f"enter number 1 or 2 or 3"
        elif song.lower() == 'n':  
            answer = input(underline("Do you want to stay in the program or leave ❓ (( Press 'S' to stay and 'E' to exitt)) ❗️ "))
            if answer.lower() == 's':
                pass
            elif answer.lower() == 'e':
                break
            else:
                raise f"enter s or e"
        else:
            raise f" You must ansower y or n"
    elif Ratings == 3:
        newlistname =["Douroubi","me and my brother","Scret Garden"]
        print(newlistname)
        song = input(cs("Do you want to hear a song 🎼 ❓ (( Press 'Y' if you agree and 'N' if you refuse )) 🎤","#ffff87"))
        if song == 'y':
            choose = int(input("🎇🎇 Which anime song do you want to hear ❓ (( Press '1' for Douroubi '2' for me and my brother '3' for Scret Garden)) ❗️ 🎇🎇"))
            if choose == 1:
                playsound('sounds/Douroubi.mp3')
                continue
            elif choose == 2:
                playsound('sounds/brother.mp3')
            elif choose == 3:
                playsound('sounds/Scret.mp3')
            else:
                raise f"enter number 1 or 2 or 3"
        elif song == 'n':  
            answer = input(underline("Do you want to stay in the program or leave ❓ (( Press 'S' to stay and 'E' to exitt)) ❗️ "))
            if answer == 's':
                pass
            elif answer == 'e':
             break
            else:
                raise f"enter s or e"
        else:
            raise f" You must ansower y or n"
    else:
        raise ValueError("You must enter number")

Q1 = input(cs("Finally 🪄, if you want to hear a motivational message 📩🪄, (( Press 'Y' if you agree and 'N' if you refuse ❓ ))", "orchid" ))
if answer == 'y':
    playsound('sounds/Message.mp3')
else:
    print("Good Bay")