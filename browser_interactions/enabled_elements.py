from selenium import webdriver
import os
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

class EnabledElements():

    def test(self):
        driver_location = 'C:\\Users\\BlazejW\\selenium\\chromedriver.exe'
        os.environ['webdriver.chrome.driver'] = driver_location
        driver = webdriver.Chrome(driver_location)
        driver.get("https://google.com")

        search_input_field = driver.find_element(By.NAME, "q")

        print(search_input_field.is_displayed())
        search_input_field.send_keys("Balmain Spring Summer 2013")
        search_input_field.send_keys(Keys.ENTER)
        sleep(4)

chrome_aut = EnabledElements()
chrome_aut.test()
