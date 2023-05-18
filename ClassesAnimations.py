


#Objects Class action
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