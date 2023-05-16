import random
from Questions import *
from playsound import playsound
from art import text2art
from colorama import Fore



class Game:

    def __init__(self,quistion:str,answer:str,isCorrect:bool = False, score:int = 0):
        self.quistion = quistion
        self.answer = answer
        self.__isCorrect = isCorrect
        self.__score = score


    def getIsCorrect(self):
        return self.__isCorrect
    
    def getLife(self) -> int:
        return self.__life
    
    def getScore(self) -> int:
        return self.__score
    
    def setIsCorrect(self,flag):
        self.__isCorrect = flag

    def setScore(self,points):
        self.__score = points

    def checkAnswer(self,answer:str) -> str:
        '''return correct (then the score will incremented) or incorrect (then the life will decremented)
        '''
        pass

    def showResult(self)-> str:
        pass




welcoming = text2art('WELCOM TO',font='tarty6')
print(Fore.MAGENTA + welcoming)
playsound('ready.mp3')
game_name = text2art('BRAIN TESTER', font='tarty7')

print(Fore.MAGENTA + game_name)
print()

while True:
    print('Select the type of the quistion from the below mneu:\n 1- General Question. \n 2- Historical Question. \n' 
          + '3- Scientific Questions. \n 4- Geographical Questions.\n 5- Exit the Game.')
    print()
    life = 3 # the user has 3 times to try if he failed more 3 times then Game over..

    if life != 0:

        try:
            choice = int(input('Please provide an integer number: '))

            if choice == 1:
                pass

            elif choice == 2:
                pass

            elif choice == 3:
                pass

            elif choice == 4:
                pass

            elif choice == 5:
                # Show the result to the user then exit the game
                pass

        except:
            TypeError('Please provide an integer number...')

    else:
        #playsound('gameover.mp3')
        game_over = text2art('GAME OVER',font='tarty6')
        print(Fore.MAGENTA + game_over)
        print('Try again next time ^,^')
        break




    
    
        