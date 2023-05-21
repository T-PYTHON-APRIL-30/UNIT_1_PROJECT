from TraineeInformation import TraineeInfo

def NumOfTrainee():
    TraineeCounter=TraineeInfo.count()
    return TraineeCounter
def TypeOfTrainee()->str:
    BMI=TraineeInfo.weight/ (TraineeInfo.height)*(TraineeInfo.height)
    if BMI in range(18.5,26):
        TraineeType="normal weight"
        print("You have a nice body keep moving**")
    elif BMI in range(26,31):
        TraineeType="over weight"
        print("Do not stop or waite go to the nearest Gym")
    elif BMI<18.5:
        TraineeType="Slim"
        print("your weight is below normal")
    elif BMI in range(31,36):
        TraineeType="first class fat"
        print("Don't worry,but you need to start your weight loss journey")
    else:
        TraineeType="second class fat"
        print("warning:you must think about High cholesterol level in the blood,High blood pressure,\nDiabetes,cardiovascular diseases,stroke,Depression,\nproblems and diseases of the joints and breathing problems sush as sleep apnea. ")
    return TraineeType