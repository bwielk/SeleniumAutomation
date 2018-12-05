from selenium import webdriver
import os

class FindByIdName():

    def test(self):
        driver_location = 'C:\\Users\\BlazejW\\selenium\\chromedriver.exe'
        os.environ['webdriver.chrome.driver'] = driver_location
        driver = webdriver.Chrome(driver_location)
        driver.get("https://learn.letskodeit.com/p/practice")
        element_by_id = driver.find_element_by_id('carselect')
        element_by_name = driver.find_element_by_name("show-hide")

        if element_by_id or element_by_name is not None:
            print("Element has been found")


chrome_aut = FindByIdName()
chrome_aut.test()