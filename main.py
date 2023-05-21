from art import *
from TraineeInformation import TraineeInfo
def traineeAge(x:int):
    Age=x
    return x


try:
    traineeName=input("kindly please enter your name:")
    if traineeName.isalpha or traineeName.isspace:
        print(f"welcome{traineeName}")
except KeyError:
    traineeName=input("please enter a correct name")
try:
    traineeAge=input("kindly please enter your age:")
except:
    traineeAge.isdigit()==False or traineeAge>200 or traineeAge<1
    traineeAge=input("please enter correct integer Age")
try:
    traineeGender=input("what is your gender(feminine or male or other)")
    if traineeGender.isalpha and traineeGender=="feminine"or traineeGender=="male"or traineeGender=="other":
     traineeG=traineeGender
except:
    traineeG=input("please enter the right word and check the spelling and write what suits you from\n these words(feminine,male,other) ")

try:
    traineeLifeStyle=input("Enter your life style active(you exercise 6 to 7 days a week)\naverage activity(you exercise 3 to 5 days a week)\nslack(you exercise 1 to 2 days a week)\nidle(you exercise just one day or Don't exercise in the week)")
    if traineeLifeStyle.lower()=="active"or traineeLifeStyle.lower()=="average activity"or traineeLifeStyle.lower()=="slack"or traineeLifeStyle.lower()=="idle":
        traineeLifSt=traineeLifeStyle
    if traineeLifeStyle.lower()=="active":
        print("you are active")
    elif traineeLifeStyle.lower()=="average activity":
        print("you are average activity")
    elif traineeLifeStyle.lower()=="slack":
        print("you are slack")
    elif traineeLifeStyle.lower()=="idle": 
        print("you are idle")
except:
    traineeLifSt=input("Opps you entered a wrong word, please check it (active,average activity,slack,idle)")
try:
    traineeWeight=input("Enter your weight in kg")
    if traineeWeight.isdigit():
        traineeW=traineeWeight
except:
    traineeW=input("sorry put you didn't entered a correct weight ")
try:
    traineeHeight=input("Enter your height in meter")
    if traineeHeight.isdigit():
        traineeH=traineeHeight
except:
    traineeH=input("warning,but do not worry,there is an error in the entering the height\n,please type it correctly in meter ")
try:
    traineeGoal=input("Enter your goal (Lose weight,OverWeight,Maintaining weight,muscle building,increased strength,participation in tournaments) " )
    if traineeGoal=="Lose weight":
        pass
    elif traineeGoal=="OverWeight":
        pass
    elif traineeGoal=="Maintaining weight":
        pass
    elif traineeGoal=="muscle building":
        pass
    elif traineeGoal=="increased strength":
        pass
    elif traineeGoal=="participation in tournaments":
        pass
except:
    traineeGoal=input("I am sorry,But you have to enter a correct goal from(Lose weight,OverWeight,Maintaining weight,muscle building,increased strength ,participation in tournaments)")
try:
    traineeMood=input("Hello dear trainee, how do you feel today?choose (great,bad,Very stressful,stressful,sick)")
    if traineeMood=="great":
        print("You look happy and that makes me happy")
    elif traineeMood=="bad":
        print("i am sorry to here that but you need ")
    elif traineeMood=="Very stressful":
        print("i am sorry to hear that but you need to go to psychiatry")
    elif traineeMood=="stressful":
        print("You can be more calm, take a deep breath and practice your hobbies")
    elif traineeMood=="sick":
        print("go to the nearest hospital")
except:
    traineeMood=input("Please enter one words as the following:great,bad,Very stressful,stressful,sick")
