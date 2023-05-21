from selenium import webdriver
from time import sleep
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
import random

class Checkphone:
    def __init__(self,phone):
        self.phone= phone
        # setup a browser
        options = Options()
        user_agents = [
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36",
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:53.0) Gecko/20100101 Firefox/53.0",
        ]
        profile = webdriver.FirefoxProfile()
        profile.set_preference("general.useragent.override",random.choice(user_agents))
        profile.set_preference("browser.privatebrowsing.autostart", True)
        options.add_argument("-headless")
        self.driver = webdriver.Firefox(options=options, firefox_profile=profile, executable_path="C:/geckodriver.exe")
        self.driver.implicitly_wait(2)
        self.driver.delete_all_cookies()

    def twitter_checker(self):
        self.driver.get('https://twitter.com/i/flow/signup')
        sleep(0.2)
        self.driver.find_element(By.XPATH,"/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/div/span/span").click()
        sleep(0.3)
        post_number = self.driver.find_element(By.XPATH,"/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/div[2]/label/div/div[2]/div/input")
        post_number.send_keys(self.phone)
        sleep(0.2)
        try:
            message = self.driver.find_element(By.XPATH,"/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/div[2]/div/div/div/div/span")
            used = "This number is already in use with other accounts. Please use another."
            if message.text == used:
                print(f"Twitter : has more than one account")
        except:
            try:
                self.driver.get("https://twitter.com/i/flow/password_reset?input_flow_data=%7B%22requested_variant%22%3A%22eyJwbGF0Zm9ybSI6IlJ3ZWIifQ%3D%3D%22%7D")
                sleep(0.7)
                post = self.driver.find_element(By.XPATH,'//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/label/div/div[2]/div/input')
                post.send_keys(self.phone)
                sleep(0.1)
                click=self.driver.find_element(By.XPATH,'//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div/div')
                click.click()
                sleep(0.1)
                verf = self.driver.find_element(By.XPATH, '//*[@id="modal-header"]/span/span').text
                mess = "Confirm your username"
                if verf == mess:
                    print("Twitter : Found ...")
                else:
                    print("Twitter : Not Found ...")
            except Exception as e:
                print(f"An error occurred: {e}")


    def name_checker(self):
        self.driver.get('http://ksanumbers.pro/')
        self.driver.find_element(By.NAME,"num").send_keys(self.phone)
        sleep(0.2)
        self.driver.find_element(By.XPATH,'//*[@id="sbtn"]/i').click()
        sleep(0.2)
        try:
            name = self.driver.find_element(By.ID, 'result').text
            if name == name:
                print(f"Name is : {name}\n")
            else:
                no_result = self.driver.find_element(By.XPATH, "/html/body/main/div/div/div/div[2]/div/li")
                message = "لا يوجد نتائج"
                if no_result.text == message:
                    return no_result.text

        except Exception as e:
            print(f"An error occurred: {e}")

    def facebook_checker(self):
        self.driver.get("https://www.facebook.com/login/identify/?ctx=recover&ars=facebook_login&from_login_screen=0")
        put_Phone= self.driver.find_element(By.ID,'identify_email')
        put_Phone.send_keys(self.phone)
        sleep(0.3)
        self.driver.find_element(By.ID,"did_submit").click()
        sleep(0.2)
        #try to check if this number is signup or available
        try:
            error= "No Search Results"
            chek= self.driver.find_element(By.XPATH,"/html/body/div[1]/div[1]/div[1]/div/div[2]/div/div/form/div/div[2]/div[1]/div[1]").text
            if chek == error:
                print(f"FaceBook : Not Found ...")
                sleep(0.2)
        except:
            print(f"FaceBook : Found...")
        self.driver.close()

    def microsoft_checker(self):
        url = "https://login.live.com/login.srf?wa=wsignin1.0&rpsnv=13&ct=1684318779&rver=7.0.6737.0&wp=MBI_SSL&wreply=https%3a%2f%2foutlook.live.com%2fowa%2f%3fexch%3d1%26nlp%3d1%26RpsCsrfState%3d10bf6aa2-c57c-f089-665e-cc07c700cfc8&id=292841&aadredir=1&CBCXT=out&lw=1&fl=dob%2cflname%2cwld&cobrandid=90015"
        self.driver.get(url)
        sleep(0.3)
        keys = self.driver.find_element(By.XPATH, '//*[@id="i0116"]')
        keys.send_keys(self.phone)
        sleep(0.3)
        try:
            next = self.driver.find_element(By.XPATH, "//*[@id='idSIButton9']")
            next.click()
            sleep(2)
            confirm = self.driver.find_element(By.XPATH, '//*[@id="loginHeader"]').text
            textconfi = "Confirm your phone number"
            if confirm == textconfi:
                next = self.driver.find_element(By.XPATH, "//*[@id='idSIButton9']")
                next.click()
                sleep(2)
            sleep(0.9)
            result = self.driver.find_element(By.XPATH, '//*[@id="usernameError"]').text
            usererror = "This phone number does not exist as a username. Please check if your number is correct."
            if result == usererror:
                print(f"Microsoft : Not Found ... \n")
        except:
            auth = self.driver.find_element(By.XPATH, '//*[@id="loginHeader"]').text
            res = "Check Microsoft Authenticator"
            if auth == res:
                print(f" Microsoft : Found ...")
            else:
                print(f"Microsoft : Found... \n")
        sleep(0.2)
        self.driver.quit()







