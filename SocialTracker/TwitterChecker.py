from selenium import webdriver
from time import sleep
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
def search_twitter(self):
    options = Options()
    profile = webdriver.FirefoxProfile()
    profile.set_preference("browser.privatebrowsing.autostart", True)
    options.add_argument('-headless')
    options.binary_location = r"C:\Program Files\Mozilla Firefox/firefox.exe"
    driver = webdriver.Firefox(options=options, firefox_profile=profile, executable_path="C:/geckodriver.exe")
    driver.implicitly_wait(2)
    driver.delete_all_cookies()
    driver.get("https://twitter.com/i/flow/signup")
    sleep(0.2)
    driver.find_element(By.XPATH,
                        "/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/div/span/span").click()
    sleep(0.3)
    post_number = driver.find_element(By.XPATH,
                                      "/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/div[2]/label/div/div[2]/div/input")
    post_number.send_keys(self)
    sleep(0.2)
    try:
        message = driver.find_element(By.XPATH,"/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/div[2]/div/div/div/div/span")
        used = "This number is already in use with other accounts. Please use another."

        if message.text == used:
            print(f"Twitter : Found...")

    except:
        print("Twitter : Not Found ...")

    driver.close()


