from selenium import webdriver
import os
from time import sleep

class BrowserInteractions():

    def test(self):
        driver_location = 'C:\\Users\\BlazejW\\selenium\\chromedriver.exe'
        os.environ['webdriver.chrome.driver'] = driver_location
        driver = webdriver.Chrome(driver_location)
        driver.get("https://learn.letskodeit.com/p/practice")
        driver.maximize_window()
        sleep(2)
        driver.minimize_window()
        sleep(2)
        driver.maximize_window()
        sleep(2)
        driver.quit()


chrome_aut = BrowserInteractions()
chrome_aut.test()
