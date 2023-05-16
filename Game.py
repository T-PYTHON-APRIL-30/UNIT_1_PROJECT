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

    def checkAnswer(self,question) -> str: # takes the question > return string
        '''return correct (then the score will incremented) or incorrect (then the life will decremented)
        '''
        if self.answer.lower() == generalQ[question].lower():
            self.setScore(self.getScore()+10)
            return 'Correct'
        else:
            return 'Incorrect'

    def showResult(self)-> str:
        pass




welcoming = text2art('WELCOM  TO',font='tarty6')
print(Fore.MAGENTA + welcoming)
#playsound('ready.mp3')
game_name = text2art('BRAIN  TESTER', font='tarty7')

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
            print()

            if choice == 1:
                question = random.choice(list(generalQ.keys()))
                print(question)
                print()
                answer = input('Your answer is: ')
                print()
                game1 = Game(question,answer)

                if game1.checkAnswer(question) == 'Correct':
                    playsound('clapping.mp3')
                    good = text2art('GOOD  JOB!', font='tarty7')
                    print(Fore.MAGENTA + good)
                    print()
                    print(f'Your Score is {game1.getScore()} and you have {life} lifes ^^')
                    print()

                else:
                    life -= 1
                    print(f'Your answer is wrong :( The correct answer is {generalQ[question]}')
                    print(f'You have {life} lifes')
                    print()
                

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
        playsound('gameover.mp3')
        game_over = text2art('GAME OVER',font='tarty6')
        print(Fore.MAGENTA + game_over)
        print(f'You reached your limits of your lifes {life}')
        print('Try again next time ^,^')
        break




    
    
        