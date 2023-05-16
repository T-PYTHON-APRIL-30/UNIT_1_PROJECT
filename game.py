import pygame
class VideoGame:
    def __init__(self, title:str, genre:str, rating:float, platform:list,url:str) :
        self.title =title
        self.genre= genre
        self.rating=rating
        self.platform= platform
        self.url=url
    
    def display_information(self):
        return f"{self.title} ({self.genre}) - Rating: {self.rating} - Platform: {self.platform}"
    
games =[
    VideoGame("call of duty:Modern Warfare® II","Shooter",9.0 ,["PC","PlayStation","Xbox"],r'D:/dawnlaodd/callofduty.png'),
    VideoGame("Overwatch","Shooter",8.5 ,["PC","PlayStation","Xbox"],""),
    VideoGame("Halo Infinite","Shooter",8.7 ,["PC","Xbox"],""),
    VideoGame("Far Cry 6","Shooter",7.7,["PlayStation","Xbox"],""),
    VideoGame("Rainbow Six Siege","Shooter",9.0,["PC","PlayStation","Xbox"],""),
    VideoGame("DOOM Eternal","Shooter",8.2,["PC","PlayStation","Xbox","Nintendo Switch"],""),
    VideoGame("The Last of Us","Narrative",9.3,["PlayStation"],""),
    VideoGame("Life is Strange","Narrative",8.3,["PC"],""),
    VideoGame("Red Dead Redemption 2","Narrative",9.3,["PlayStation","PC","Xbox"],""),
    VideoGame("The Witcher 3:Wild Hunt","Narrative",9.2,["PlayStation","Xbox","Nintendo Switch"],""),
    VideoGame("The Legend of Zelda","Narrative",9.7,["Nintendo Switch"],""),
    VideoGame("FIFA 23","Sports",7.4,["PC","PlayStation","Xbox"],""),
    VideoGame("NBA 2K21","Sports",7.1 ,["PC","PlayStation","Xbox"],""),
    VideoGame("Rocket League","Sports",8.0,["PC","PlayStation","Xbox","Nintendo Switch"],""),
    VideoGame("Hollow Knight","Platformer",8.9,["PC","Xbox","Nintendo Switch"],""),
    VideoGame("Crash Bandicoot N. Sane Trilogy","Platformer",8.0,["PlayStation","Xbox"],"") 
]


'''from PIL import Image                                                                                
img = Image.open('D:\dawnlaodd\callOfDutyPoster.png')
img.show() 
pygame.init()'''
def image_function():
    displayWidth = 1270
    displayHeight =600
    surface =pygame.display.set_mode((displayWidth,displayHeight))
    pygame.display.set_caption('Image')
    displayImage=pygame.image.load(games[0].url)
    while True:
        surface.fill((255,255,255))
        surface.blit(displayImage,(0,0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            pygame.display.update()

'''print(games[0].display_info())
image_function()'''
