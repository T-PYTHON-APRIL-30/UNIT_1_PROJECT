import random
import time
from Questions import *
from playsound import playsound
from art import text2art, aprint
from colorama import Fore,Style


global life, totalScore, game1
life = 5     # the user has 5 lifes to try if he failed more than 5 times then Game over..
totalScore = 0 # initilized the total score with 0 to increment it after every correct answer..


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
            return 'Not bad, but you have to improve your knowledge!'
        else:
            return 'Better to increase your knowledge!!!'

def cheer():
    playsound('C:\\Users\\amani\\Documents\\TwaiqPythonCamp\\UNIT_1_PROJECT\\clapping.mp3')
    good = text2art('GOOD  JOB!', font='tarty7')
    print(Fore.CYAN + good)
    print()
    aprint("happy", number=3)
    print(Style.RESET_ALL)
    print()

def wrong(tryingTime:int):
    x = text2art('XXX', 'tarty7')
    print(Fore.RED + x)
    print()
    playsound('wrongg.mp3')
    print(f'You have {tryingTime} lifes left')
    print(Style.RESET_ALL)

def goodBye():
    print(Fore.MAGENTA + 'Thank you for using BRAIN TESTER GAME ♡⸜(˶˃ ᵕ ˂˶)⸝♡')
    goodbye = text2art('GoodBye','tarty7')
    print(goodbye)
    print(Style.RESET_ALL)
    print()

def decrementLife():
    return lambda num : num - 1

'''def countdown(t):
    
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        t-= 1'''

 

welcoming = text2art('WELCOM  TO',font='tarty6')
print(Fore.MAGENTA + welcoming)
playsound('readyg.mp3')
game_name = text2art('BRAIN  TESTER', font='tarty7')
print(Fore.MAGENTA + game_name)
print(Style.RESET_ALL)
print()



while life !=0 :

    print('Select the type of the question from the below mneu:\n 1- General Question. \n 2- Historical Question. \n' 
          + '3- Scientific Questions. \n 4- Geographical Questions.\n 5- Exit the Game.')
    print()

    
    try:
        choice = int(input(Fore.MAGENTA + 'Please provide an integer number: '))
        print(Style.RESET_ALL)
        print()

        if choice == 1:

            questionType = text2art('General Question','cybermedium')
            print(Fore.MAGENTA + questionType)
            print(Style.RESET_ALL)
            print()

            question = random.choice(list(generalQ.keys()))
            print(question)
            print()

            print('You have 15 seconds to answer the question..')
            print()

            timer_duration = 15
            start_time = time.time()

            answer = input(Fore.MAGENTA + 'Your answer is: ')
            print(Style.RESET_ALL)
            print()
            
            elapsed_time = time.time() - start_time

            print(f'You took {round(elapsed_time,2)} seconds')
            print()

            game1 = Game(question,answer)

            if elapsed_time < timer_duration:

                if game1.checkAnswer(generalQ):
                    cheer()
                    totalScore += game1.getScore()
                    print(Fore.CYAN + f'You got extra {game1.getScore()} points. \n Your total Score is {totalScore}.'
                        + f'\n and you have {life} lifes ( ˶ˆᗜˆ˵ )')
                    print(Style.RESET_ALL)
                    print()

                else:
                    decrement = decrementLife()
                    life = decrement(life)
                    wrong(life)
                    print(Fore.RED + f'Your answer is wrong (◡︵◡) \n The correct answer is {generalQ[question]}')
                    print(Style.RESET_ALL)
                    print()
            
            else:
                print(Fore.RED + "SORRY, Time out try again!")
                decrement = decrementLife()
                life = decrement(life)
                wrong(life)


        elif choice == 2:

            questionType = text2art('Historical Question','cybermedium')
            print(Fore.MAGENTA + questionType)
            print(Style.RESET_ALL)
            print()

            question = random.choice(list(historicalQ.keys()))
            print(question)
            print()

            print('You have 15 seconds to answer the question..')
            print()

            timer_duration = 15
            start_time = time.time()

            answer = input(Fore.MAGENTA + 'Your answer is: ')
            print(Style.RESET_ALL)
            print()
            
            elapsed_time = time.time() - start_time

            print(f'You took {round(elapsed_time,2)} seconds')
            print()

            game2 = Game(question,answer)

            if elapsed_time < timer_duration:

                if game2.checkAnswer(historicalQ):
                    cheer()
                    totalScore += game2.getScore()
                    print(Fore.CYAN + f'You got extra {game2.getScore()} points. \n Your total Score is {totalScore}.'
                        + f'\n and you have {life} lifes ( ˶ˆᗜˆ˵ )')
                    print(Style.RESET_ALL)
                    print()

                else:
                    decrement = decrementLife() # method that use lambds
                    life = decrement(life)
                    wrong(life)
                    print(Fore.RED + f'Your answer is wrong (◡︵◡) \n The correct answer is {historicalQ[question]}')
                    print(Style.RESET_ALL)
                    print()
            
            else:
                print(Fore.RED + "SORRY, Time out try again!")
                decrement = decrementLife()
                life = decrement(life)
                wrong(life)

        elif choice == 3:

            questionType = text2art('Scientific Question','cybermedium')
            print(Fore.MAGENTA + questionType)
            print(Style.RESET_ALL)
            print() 

            question = random.choice(list(scientificQ.keys()))
            print(question)
            print()

            print('You have 15 seconds to answer the question..')
            print()

            timer_duration = 15
            start_time = time.time()

            answer = input(Fore.MAGENTA + 'Your answer is: ')
            print(Style.RESET_ALL)
            print()
            
            elapsed_time = time.time() - start_time

            print(f'You took {round(elapsed_time,2)} seconds')
            print()

            game3 = Game(question,answer)

            if elapsed_time < timer_duration:

                if game3.checkAnswer(scientificQ):
                    cheer()
                    totalScore += game3.getScore()
                    print(Fore.CYAN + f'You got extra {game3.getScore()} points. \n Your total Score is {totalScore}.'
                        + f'\n and you have {life} lifes ( ˶ˆᗜˆ˵ )')
                    print(Style.RESET_ALL)
                    print()

                else:
                    decrement = decrementLife()
                    life = decrement(life)
                    wrong(life)
                    print(Fore.RED + f'Your answer is wrong (◡︵◡) \n The correct answer is {scientificQ[question]}')
                    print(Style.RESET_ALL)
                    print()
            
            else:
                print(Fore.RED + "SORRY, Time out try again!")
                decrement = decrementLife()
                life = decrement(life)
                wrong(life)


        elif choice == 4:
            questionType = text2art('Geographical Question','cybermedium')
            print(Fore.MAGENTA + questionType)
            print(Style.RESET_ALL)
            print()

            question = random.choice(list(geographicalQ.keys()))
            print(question)
            print()

            print('You have 15 seconds to answer the question..')
            print()

            timer_duration = 15
            start_time = time.time()

            answer = input(Fore.MAGENTA + 'Your answer is: ')
            print(Style.RESET_ALL)
            print()
            
            elapsed_time = time.time() - start_time

            print(f'You took {round(elapsed_time,2)} seconds')
            print()

            game4 = Game(question,answer)

            if elapsed_time < timer_duration:

                if game4.checkAnswer(geographicalQ):
                    cheer()
                    totalScore += game4.getScore()
                    print(Fore.CYAN + f'You got extra {game4.getScore()} points. \n Your total Score is {totalScore}.'
                        + f'\n and you have {life} lifes ( ˶ˆᗜˆ˵ )')
                    print(Style.RESET_ALL)
                    print()

                else:
                    decrement = decrementLife()
                    life = decrement(life)
                    wrong(life)
                    print(Fore.RED + f'Your answer is wrong (◡︵◡) \n The correct answer is {geographicalQ[question]}')
                    print(Style.RESET_ALL)
                    print()
            
            else:
                print(Fore.RED + "SORRY, Time out try again!")
                decrement = decrementLife()
                life = decrement(life)
                wrong(life)

        elif choice == 5:
            # Show the result to the user then exit the game
            print(f'Your total score is {totalScore}, {game1.showResults(totalScore)}')
            print()
            goodBye()
            break

        else:
            print(Fore.RED + 'Please enter a number from 1 to 5...')
            print(Style.RESET_ALL)
            print()

    except TypeError:
        raise TypeError('Please provide an integer number...')
    
          

if life == 0:

    game_over = text2art('GAME OVER',font='tarty6')
    print(Fore.RED + game_over)
    print()
    playsound('gameover.mp3')
    print(f'You reached your limits of your lifes {life}')
    print( f'You loose the game Try again next time (ㅠ﹏ㅠ)')
    print(Style.RESET_ALL)
    print()
    goodBye()
        




    
    
        