from selenium import webdriver
import os

class FindByIdName():

    def test(self):
        driver_location = 'C:\\Users\\BlazejW\\selenium\\chromedriver.exe'
        os.environ['webdriver.chrome.driver'] = driver_location
        driver = webdriver.Chrome(driver_location)
        driver.get("https://learn.letskodeit.com/p/practice")
        element_by_xpath = driver.find_element_by_xpath(
            '//*[@id="radio-btn-example"]')
        element_by_css = driver.find_element_by_css_selector("#bmwradio")

        if element_by_xpath or element_by_css is not None:
            print("Element has been found by Xpath and CSS")


chrome_aut = FindByIdName()
chrome_aut.test()