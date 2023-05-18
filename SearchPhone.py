from selenium import webdriver
from time import sleep
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By

#set a browser
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


    def search_name(self):
        driver.get('http://ksanumbers.pro/')
        driver.find_element(By.NAME,"num").send_keys(self.phone)
        sleep(0.2)
        driver.find_element(By.XPATH,'//*[@id="sbtn"]/i').click()
        sleep(0.2)
        try:
            name = driver.find_element(By.ID, 'result').text
            if name == name:
                print(f"Name is : {name}")

            else:
                no_result = driver.find_element(By.XPATH, "/html/body/main/div/div/div/div[2]/div/li")
                message = "لا يوجد نتائج"
                if no_result.text == message:
                    return no_result.text

        except Exception as e:
            print(f"An error occurred: {e}")

    def search_facebook(self):
        global driver
        driver.get("https://www.facebook.com/login/identify/?ctx=recover&ars=facebook_login&from_login_screen=0")
        put_Phone= driver.find_element(By.ID,'identify_email')
        put_Phone.send_keys(self.phone)
        sleep(0.3)
        driver.find_element(By.ID,"did_submit").click()
        sleep(0.2)
        #try to check if this number is sign up or available
        try:
            error= "No Search Results"
            chek= driver.find_element(By.XPATH,"/html/body/div[1]/div[1]/div[1]/div/div[2]/div/div/form/div/div[2]/div[1]/div[1]").text
            if chek == error:
                print(f"FaceBook : Not Found ...")
                sleep(0.2)
        except:
            print(f"\nFaceBook : Found...")










