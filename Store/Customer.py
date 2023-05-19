import pyttsx3

'''engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id) 
rate = engine.getProperty('rate')                       
engine.setProperty('rate', 115)
engine.say("Hello, my name is ahmed please tell me about your self")
engine.runAndWait()'''

class customer:
    def __init__(self,engine=None):
        self.__engine = engine or pyttsx3.init()

    def text_to_speech(self,text:str):
        voices = self.__engine.getProperty('voices')
        self.__engine.setProperty('Voice', voices[1].id)
        self.__engine.getProperty('rate')
        self.__engine.setProperty('rate',115)
        self.__engine.say(text)
        self.__engine.runAndWait()
    def text_to_speech_fast(self,text:str):
        voices = self.__engine.getProperty('voices')
        self.__engine.setProperty('Voice', voices[1].id)
        self.__engine.getProperty('rate')
        self.__engine.setProperty('rate',600)
        self.__engine.say(text)
        self.__engine.runAndWait()
#customer1 = customer()
#customer1.text_to_speech("Chief let's program")
