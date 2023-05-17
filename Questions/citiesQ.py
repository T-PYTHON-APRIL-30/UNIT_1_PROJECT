from Questions import cheackScoreTime as finalScore
import time
class Answer:
    def __init__(self,answer:str):
        self.answer = answer
    def correctAnswer(self):
        return print(f"\nWrong Guess...\n\tThe correct naswer is ( {self.answer} ).\n")

class Hint(Answer):
    def __init__(self, answer: str) :
        super().__init__(answer)
    def correctAnswer(self):
        return super().correctAnswer()
    
    def hintOne(self):
        return print("\n\tI've a sea!\n")
    
    def hintTwo(self):
        return print("\n\tI'm so crowded in Ramadan!\n")
    
    def hintThree(self):
        return print("\n\tThere's country in me!\n")

answer1 = Hint("Jeddah")
answer2 = Hint("Mecca")
answer3 = Hint("Vatican city")

'''def cheackTime(time):
    if time < 5.0 :
        return print(f"\n\tThat was fast ! You takes only {time} seconds.\n")
    elif time > 25.0 :
        return print(f"\n\tThat was late ! You takes {time} seconds.\n")
    else:
        return print(f"\n\tYou takes {time} seconds.\n")

def cheackScore(total,time):
    if time >= 25.0 :
        total -= 0.25
    if 0.0 >= total :
        return print("\n\tYou didn't get any answer correct!\n")
    elif 0.0 < total < 2.0 :
        return print(f"\n\tUmmm ! You got {total}/5 !\n")
    elif 2.0 <= total < 4.0 :
        return print(f"\n\tNice ! You got {total}/5 !\n")
    elif total >= 4.0 :
        return print(f"\n\tCongrats !! You got {total}/5 !\n")'''

def puzzle():
    score = []
    start = time.time()
    print("\n\tI'm hot in the summer and hot in the winter !\n")
    print("Who I am?")
    guess1 = input("[ 'R' -> Riyadh - 'H' -> Hail - 'J' -> Jeddah - 'T' -> Taif ]\n'h' -> For a hint\nEnter: ").lower()
    if guess1 == "j":
        score.append(1.5)
    elif guess1 == "h":
        score.append(-0.25)
        answer1.hintOne()
        print("Who am I?")
        guess1h = input("[ 'R' -> Riyadh - 'H' -> Hail - 'J' -> Jeddah - 'T' -> Taif ]\nEnter: ").lower()
        if guess1h == "j":
            score.append(1.5)
        elif guess1h != "j":
            answer1.correctAnswer()
            print("*"*50)
    elif guess1 != "j" and guess1 != "h":
        answer1.correctAnswer()
        print("*"*50)

    print("\n\tMy visitores are more than my population!\n")
    print("Who I am?")
    guess2 = input("[ 'Q' -> Qassim - 'M' -> Mecca - 'K' -> Kuwait - 'A' -> Alain ]\n'h' -> For a hint\nEnter: ").lower()
    if guess2 == "m":
        score.append(1.5)
    elif guess2 == "h":
        score.append(-0.25)
        answer2.hintTwo()
        print("Who am I?")
        guess2h = input("[ 'Q' -> Qassim - 'M' -> Mecca - 'K' -> Kuwait - 'A' -> Alain ]\nEnter: ").lower()
        if guess2h == "m":
            score.append(1.5)
        elif guess2h != "m":
            answer2.correctAnswer()
            print("*"*50)
    elif guess2 != "m" and guess2 != "h":
        answer2.correctAnswer()
        print("*"*50)

    print("\n\tI'm the smallest city in the world!\n")
    print("Who I am?")
    guess3 = input("[ 'V' -> Vatican city - 'Y' -> Yanbu - 'M' -> Madrid - 'B' -> Bahrain ]\n'h' -> For a hint\nEnter: ").lower()
    if guess3 == "v":
        score.append(2)
    elif guess3 == "h":
        score.append(-0.25)
        answer3.hintThree()
        print("Who am I?")
        guess3h = input("[ 'V' -> Vatican city - 'Y' -> Yanbu - 'M' -> Madrid - 'B' -> Bahrain ]\nEnter: ").lower()
        if guess3h == "v":
            score.append(2)
        elif guess3h != "i":
            answer3.correctAnswer()
            print("*"*50)
    elif guess3 != "i" and guess3 != "h":
        answer3.correctAnswer()
        print("*"*50)
    end = time.time()

    timeTaken = round((end - start),2)
    
    scoreFun = lambda scoreList : scoreList[0] if len(scoreList) == 1 else scoreList[0] + scoreFun(scoreList[1:])
    try:
        totalScore = scoreFun(score)
        finalScore.cheackScore(totalScore,timeTaken)
        finalScore.cheackTime(timeTaken)
    except:
        print("\n\tYou didn't get any answer correct!\n")