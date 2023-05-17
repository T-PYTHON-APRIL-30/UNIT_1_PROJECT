import random
from Questions import *
from playsound import playsound
from art import text2art, aprint
from colorama import Fore



class Game:

    def __init__(self,question:str,answer:str,isCorrect:bool = False, score:int = 0):
        self.question = question
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

    def checkAnswer(self,questionsDict:str) -> str: # takes the question > return string
        '''return True if the answer is correct (then the score will incremented) or Falls otherwise (then the life will decremented)
        '''
        if self.answer.lower() == questionsDict[self.question].lower():
            self.setScore(self.getScore()+10)
            self.setIsCorrect(True)
            return self.getIsCorrect()
        else:
            return self.getIsCorrect()

    def showResults(self, total:int)-> str:
        if total >= 90:
            return 'Your knowledge is excellent!'
        elif total >= 80:
            return 'You have a very good knowledge!'
        elif total >= 70:
            return 'Good!'
        elif total >= 60:
            return 'Not bad, but you have to develope your knowledge!'
        else:
            return 'Better to increase your knowledge!!!'

def cheer():
    playsound('C:\\Users\\amani\\Documents\\TwaiqPythonCamp\\UNIT_1_PROJECT\\clapping.mp3')
    good = text2art('GOOD  JOB!', font='tarty7')
    print(Fore.MAGENTA + good)
    print()
    aprint("happy", number=3)
    print()



welcoming = text2art('WELCOM  TO',font='tarty6')
print(Fore.MAGENTA + welcoming)
playsound('readyg.mp3')
game_name = text2art('BRAIN  TESTER', font='tarty7')

print(Fore.MAGENTA + game_name)
print()


global player1, player2, player3, player4, life, totalScore
life = 5     # the user has 5 lifes to try if he failed more than 5 times then Game over..


while True:
    print('Select the type of the quistion from the below mneu:\n 1- General Question. \n 2- Historical Question. \n' 
          + '3- Scientific Questions. \n 4- Geographical Questions.\n 5- Exit the Game.')
    print()

    if life != 0:

        try:
            choice = int(input('Please provide an integer number: '))
            print()

            if choice == 1:
                questionType = text2art('General Question','white_bubble')
                print(questionType)
                print()
                question = random.choice(list(generalQ.keys()))
                print(question)
                print()
                answer = input('Your answer is: ')
                print()
                game1 = Game(question,answer)

                if game1.checkAnswer(generalQ) == True:
                    cheer()
                    print(f'You got {game1.getScore()} points and you have {life} lifes ^^')
                    print()

                else:
                    playsound('wrongg.mp3')
                    life -= 1
                    print(f'Your answer is wrong :( The correct answer is {generalQ[question]}')
                    print(f'You have {life} lifes')
                    print()
                

            elif choice == 2:
                questionType = text2art('Historical Question','white_bubble')
                print(questionType)
                print()
                question = random.choice(list(historicalQ.keys()))
                print(question)
                print()
                answer = input('Your answer is: ')
                print()
                game2 = Game(question,answer)

                if game2.checkAnswer(historicalQ) == True:
                    cheer()
                    print(f'You got {game2.getScore()} points, and you have {life} lifes ^^')
                    print()

                else:
                    life -= 1
                    playsound('wrongg.mp3')
                    print(f'Your answer is wrong :( The correct answer is {historicalQ[question]}')
                    print(f'You have {life} lifes')
                    print()

            elif choice == 3:
                questionType = text2art('Scientific Question','white_bubble')
                print(questionType)
                print() 
                question = random.choice(list(scientificQ.keys()))
                print(question)
                print()
                answer = input('Your answer is: ')
                print()
                game3 = Game(question,answer)

                if game3.checkAnswer(scientificQ) == True:
                    cheer()
                    print(f'You got {game3.getScore()} points, and you have {life} lifes ^^')
                    print()

                else:
                    life -= 1
                    playsound('wrongg.mp3')
                    print(f'Your answer is wrong :( The correct answer is {scientificQ[question]}')
                    print(f'You have {life} lifes')
                    print()

            elif choice == 4:
                questionType = text2art('Geographical Question','white_bubble')
                print(questionType)
                print()
                question = random.choice(list(geographicalQ.keys()))
                print(question)
                print()
                answer = input('Your answer is: ')
                print()
                game4 = Game(question,answer)

                if game4.checkAnswer(geographicalQ) == True:
                    cheer()
                    print(f'You got {game4.getScore()} points, and you have {life} lifes ^^')
                    print()

                else:
                    life -= 1
                    playsound('wrongg.mp3')
                    print(f'Your answer is wrong :( The correct answer is {geographicalQ[question]}')
                    print(f'You have {life} lifes')
                    print()

            elif choice == 5:
                # Show the result to the user then exit the game
                totalScore = game1.getScore() + game2.getScore() + game3.getScore() + game4.getScore()
                print(f'Your total score is {totalScore}, {game1.showResults(totalScore)}')
                print()
                print('Thank you for using BRAIN TESTER GAME ^,^')
                print()
                break

            else:
                print('Please enter a number from 1 to 5...')
                print()

        except TypeError:
            raise TypeError('Please provide an integer number...')
          

    elif life == 0:
        game_over = text2art('GAME OVER',font='tarty6')
        print(Fore.MAGENTA + game_over)
        print()
        playsound('gameover.mp3')
        print(f'You reached your limits of your lifes {life}')
        print(f'You loose the game Try again next time ^,^')
        print()
        break




    
    
        