url = "https://login.live.com/login.srf?wa=wsignin1.0&rpsnv=13&ct=1684318779&rver=7.0.6737.0&wp=MBI_SSL&wreply=https%3a%2f%2foutlook.live.com%2fowa%2f%3fexch%3d1%26nlp%3d1%26RpsCsrfState%3d10bf6aa2-c57c-f089-665e-cc07c700cfc8&id=292841&aadredir=1&CBCXT=out&lw=1&fl=dob%2cflname%2cwld&cobrandid=90015"
from selenium import webdriver
from time import sleep
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

def Microsofot_checker(self):
    options = Options()
    profile = webdriver.FirefoxProfile()
    profile.set_preference("browser.privatebrowsing.autostart", True)
    options.add_argument('-headless')
    options.binary_location = r"C:\Program Files\Mozilla Firefox/firefox.exe"
    driver = webdriver.Firefox(options=options, firefox_profile=profile, executable_path="C:/geckodriver.exe")
    driver.implicitly_wait(2)
    driver.delete_all_cookies()
    driver.get(url)
    sleep(0.9)
    keys= driver.find_element(By.XPATH,'//*[@id="i0116"]')
    keys.send_keys(self)
    sleep(0.9)
    next= driver.find_element(By.XPATH,"//*[@id='idSIButton9']").click()
    sleep(0.9)
    next1= driver.find_element(By.XPATH,'//*[@id="idSIButton9"]').click()
    try:
        result= driver.find_element(By.XPATH,'//*[@id="usernameError"]').text
        usererror= "This phone number does not exist as a username. Please check if your number is correct."
        if result == usererror:
            print(f"Microsoft : Not Found ... \n")
    except:
        print(f"Microsoft : Found... \n")
    #keys.send_keys(self[3:])
    sleep(0.2)
    driver.close()
