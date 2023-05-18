from selenium import webdriver
from time import sleep
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import csv
options = Options()
profile = webdriver.FirefoxProfile()
profile.set_preference("browser.privatebrowsing.autostart", True)
options.add_argument('-headless')
options.binary_location = r"C:\Program Files\Mozilla Firefox/firefox.exe"
driver = webdriver.Firefox(options=options, firefox_profile=profile, executable_path="C:/geckodriver.exe")
driver.implicitly_wait(2)
driver.delete_all_cookies()
sleep(0.5)

class Checkphone:

    def __init__(self,phone):
        self.phone= phone

    def search_facebook(self):
        global driver
        driver.get("https://www.facebook.com/login/identify/?ctx=recover&ars=facebook_login&from_login_screen=0")
        put_Phone= driver.find_element(By.ID,'identify_email')
        put_Phone.send_keys(self.phone)
        sleep(0.3)
        driver.find_element(By.ID,"did_submit").click()
        sleep(0.5)
        #try to check if this number is sign up or available
        try:
            error= "No Search Results"
            chek= driver.find_element(By.XPATH,"/html/body/div[1]/div[1]/div[1]/div/div[2]/div/div/form/div/div[2]/div[1]/div[1]").text
            if chek == error:
                print(f"FaceBook : Not Found ...")
                sleep(3)
        except:
            print(f"FaceBook : Found")









