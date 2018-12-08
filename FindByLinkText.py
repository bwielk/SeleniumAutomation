from selenium import webdriver
import os

class FindByLinkText():

    def test(self):
        driver_location = 'C:\\Users\\BlazejW\\selenium\\chromedriver.exe'
        os.environ['webdriver.chrome.driver'] = driver_location
        driver = webdriver.Chrome(driver_location)
        driver.get("https://learn.letskodeit.com/p/practice")
        element_by_link_text_login = driver.find_element_by_link_text("Login")
        element_by_partial_link_text_practice = driver.find_element_by_partial_link_text("Pra")

        if element_by_link_text_login or element_by_partial_link_text_practice is not None:
            print("Elements have been found")


chrome_aut = FindByLinkText()
chrome_aut.test()