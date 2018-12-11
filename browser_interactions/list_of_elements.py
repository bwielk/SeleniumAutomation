from selenium import webdriver
import os
from selenium.webdriver.common.by import By
from time import sleep

class ListOfElements():

    def test(self):
        driver_location = 'C:\\Users\\BlazejW\\selenium\\chromedriver.exe'
        os.environ['webdriver.chrome.driver'] = driver_location
        driver = webdriver.Chrome(driver_location)
        driver.get("https://learn.letskodeit.com/p/practice")
        radio_buttons_list = driver.find_elements(By.XPATH, "//input[contains(@type,'radio')and contains(@name,'cars')]")
        print(len(radio_buttons_list))

        for radio in radio_buttons_list:
            radio.click()
            print("clicked")
            sleep(2)

chrome_aut = ListOfElements()
chrome_aut.test()
