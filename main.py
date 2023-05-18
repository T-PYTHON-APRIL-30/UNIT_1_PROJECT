from playsound import playsound
from stringcolor import * 
from ClassesAnimations import *
playsound('sounds/WelcomeSpeaceToon.mp3')
print(cs("🎊🎊😍 This Is a Program For Animations 😍🎊🎊 ","orchid" ))



while True:
    Ratings = int(input("Do you prefer action🎬 or comedy 🥳 or drama🔮 ❓ (( Press 1 for the ACTION, 2 for COMEDY, 3 for DRAMA Or 0 for exit))❓"))
    if Ratings == 1:
        newlistname =  ["Conan","digitalis jungle","Gundam Wings"]
        filtered_list = list(filter(lambda element: element < element[3], newlistname ))
        print("the filtered list is :")
        print(f"-{filtered_list}")
        q2 = int(input("Spisfic animi 1 conan 2 ff 3 ttt"))
        if q2 == 1:
                animeact1 = action("Conan","action",9.9,10)
                print(animeact1.anime_informations("Conan","action",9.9,5))
        elif q2 == 2:
                animeact2 = action("digitalis jungle","action",9.9,7)
                print(animeact2.anime_informations("digitalis jungle","action",9.9,8))
        elif q2 == 3:
                animeact3 = action("Gundam Wings","action",9.9,10)
                print(animeact3.anime_informations("Gundam Wings","action",9.9,1))
        else:
            pass

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
         try:
            answer = input(underline("Do you want to stay in the program or leave ❓ ((2 Press 'S' to stay and 'E' to exitt)) ❗️ "))
            if answer.lower() == 's':
                pass
            elif answer.lower() == 'e':
                break
         except:
             raise ValueError("Only a character is required")
    elif Ratings == 2:
        newlistname = ["Kudo and Modo","Moca","police Academy"]
        print(f"- {newlistname}")
        q2 = int(input("Spisfic animi 1 conan 2 ff 3 ttt"))
        if q2 == 1:
                animecom1 = comedy("Kudo and Modo","comedy",9.9,9)
                print(animecom1.anime_informations("Kudo and Modo","comedy",9.9,9))
        elif q2 == 2:
                animecom2 = comedy("Moca","comedy",9.9,10)
                print(animecom2.anime_informations("Moca","comedy",9.9,10))
        elif q2 == 3:
                animecom3 = comedy("police Academy","comedy",9.9,10)
                print(animecom3.anime_informations("olice Academy","comedy",9.9,10))
        else:
            pass
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
            answer = input(underline("Do you want to stay in the program or leave ❓ (( 3Press 'S' to stay and 'E' to exitt)) ❗️ "))
            if answer.lower() == 's':
                print("good chooiss")
            elif answer.lower() == 'e':
                break
            else:
                raise f"enter s or e"
        else:
            raise f" You must ansower y or n"
    elif Ratings == 3:
        newlistname =["Douroubi","me and my brother","Scret Garden"]
        print(newlistname)
        q2 = int(input("Spisfic animi 1 conan 2 ff 3 ttt"))
        if q2 == 1:
                    animendrama1 = drama("Douroubi","drama",9.9,10)
                    print(animendrama1.anime_informations("Douroubi","drama",9.9,1))
        elif q2 == 2:
                    animedrama2 = drama("me and my brother","drama",9.9,6)
                    print(animedrama2.anime_informations("me and my brother","drama",9.9,6))
        elif q2 == 3:
                    animedrama3 = drama("Scret Garden","drama",9.9,10)
                    print(animedrama3.anime_informations("Scret Garden","drama",9.9,10))
        else:
                pass
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
            answer = input(underline("Do you want to stay in the program or leave ❓ (( 4Press 'S' to stay and 'E' to exitt)) ❗️ "))
            if answer == 's':
                pass
            elif answer == 'e':
             break
            else:
                raise f"enter s or e"
        else:
            raise f" You must ansower y or n"
    elif Ratings == 0:
         break
    else:
        raise ValueError("You must enter number")

Q1 = input(cs("Finally 🪄, if you want to hear a motivational message 📩🪄, (( Press 'Y' if you agree and 'N' if you refuse ❓ ))", "orchid" ))
if Q1.lower() == 'y':
        playsound('sounds/Message.mp3')
else:
        print("Good Bay")