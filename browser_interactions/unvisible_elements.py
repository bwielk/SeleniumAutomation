from selenium import webdriver
import os
from time import sleep
from selenium.webdriver.support.select import Select

class UnvisibleElements():

    def test(self):
        driver_location = 'C:\\Users\\BlazejW\\selenium\\chromedriver.exe'
        os.environ['webdriver.chrome.driver'] = driver_location
        driver = webdriver.Chrome(driver_location)
        driver.get("https://learn.letskodeit.com/p/practice")
        driver.maximize_window()


chrome_aut = UnvisibleElements()
chrome_aut.test()
