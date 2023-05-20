import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)
class VideoGame:
    def __init__(self, title:str, genre:str, rating:float, platform:list,url:str) :
        self.title =title
        self.genre= genre
        self.rating=rating
        self.platform= platform
        self.url=url
    
    def display_information(self,platform:str)->str:
        return f"{Fore.MAGENTA}{self.title} {Fore.YELLOW}({self.genre}){Fore.MAGENTA} - Rating:{Fore.YELLOW} {self.rating}{Fore.MAGENTA} - Platform:{Fore.YELLOW} {platform.upper()}"
    
games:list =[
    VideoGame("call of duty:Modern Warfare2","Shooter",9.0 ,["PC","PlayStation","Xbox"],r'D:/dawnlaodd/images/callofduty.png'),
    VideoGame("Overwatch","Shooter",8.5 ,["PC","PlayStation","Xbox","Nintendo Switch"],r'D:/dawnlaodd/images/overwhatch.png'),
    VideoGame("Halo Infinite","Shooter",8.7 ,["PC","Xbox"],r'D:/dawnlaodd/images/haloinfinite.png'),
    VideoGame("Far Cry 6","Shooter",7.7,["PlayStation","Xbox"],r'D:/dawnlaodd/images/farcry6.png'),
    VideoGame("Rainbow Six Siege","Shooter",9.0,["PC","PlayStation","Xbox"],r'D:/dawnlaodd/images/rainbosix.png'),
    VideoGame("DOOM Eternal","Shooter",8.2,["PC","PlayStation","Xbox","Nintendo Switch"],r'D:/dawnlaodd/images/doometernal.png'),
    VideoGame("The Last of Us","Narrative",9.3,["PlayStation"],r'D:/dawnlaodd/images/thelastofus.png'),
    VideoGame("Life is Strange","Narrative",8.3,["PC"],r'D:/dawnlaodd/images/LifeisStrange.png'),
    VideoGame("Red Dead Redemption 2","Narrative",9.3,["PlayStation","PC","Xbox"],r'D:/dawnlaodd/images/reddead2.png'),
    VideoGame("The Witcher 3:Wild Hunt","Narrative",9.2,["PlayStation","Xbox","Nintendo Switch"],r'D:/dawnlaodd/images/thewitcher3.png'),
    VideoGame("The Legend of Zelda","Narrative",9.7,["Nintendo Switch"],r'D:/dawnlaodd/images/Zelda.png'),
    VideoGame("FIFA 23","Sports",7.4,["PC","PlayStation","Xbox"],r'D:/dawnlaodd/images/fifa23.png'),
    VideoGame("NBA 2K21","Sports",7.1 ,["PC","PlayStation","Xbox"],r'D:/dawnlaodd/images/nba2k21.png'),
    VideoGame("Rocket League","Sports",8.0,["PC","PlayStation","Xbox","Nintendo Switch"],r'D:/dawnlaodd/images/rocketleague.png'),
    VideoGame("Hollow Knight","Platformer",8.9,["PC","Xbox","Nintendo Switch"],r'D:/dawnlaodd/images/hollowknight.png'),
    VideoGame("Crash Bandicoot N. Sane Trilogy","Platformer",8.0,["PlayStation","Xbox"],r'D:/dawnlaodd/images/Crash.png') 
]

platform_list:list= ["PC","PlayStation","Xbox","Nintendo Switch"]

genre_list:list=["Shooter","Narrative","Sports","Platformer"]

