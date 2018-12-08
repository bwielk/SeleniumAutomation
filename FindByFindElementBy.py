from selenium import webdriver
from selenium.webdriver.common.by import By
import os

class FindByFindElementBy():

    def test(self):
        driver_location = 'C:\\Users\\BlazejW\\selenium\\chromedriver.exe'
        os.environ['webdriver.chrome.driver'] = driver_location
        driver = webdriver.Chrome(driver_location)
        driver.get("https://learn.letskodeit.com/p/practice")


        if element_by_id or element_by_name is not None:
            print("Element has been found")


chrome_aut = FindByFindElementBy()
chrome_aut.test()