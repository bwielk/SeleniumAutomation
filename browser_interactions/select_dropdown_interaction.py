from selenium import webdriver
import os
from time import sleep
from selenium.webdriver.support.select import Select

class SelectDropdownInteraction():

    def test(self):
        driver_location = 'C:\\Users\\BlazejW\\selenium\\chromedriver.exe'
        os.environ['webdriver.chrome.driver'] = driver_location
        driver = webdriver.Chrome(driver_location)
        driver.get("https://learn.letskodeit.com/p/practice")
        driver.maximize_window()

        dropdown = driver.find_element_by_id('carselect')
        select = Select(dropdown)
        #select by value
        select.select_by_value("honda")
        sleep(4)
        #select by name
        select.select_by_visible_text("Benz")
        sleep(4)
        #select by index
        select.select_by_index(0)
        sleep(4)
        select.select_by_visible_text("Benz")
        sleep(4)

chrome_aut = SelectDropdownInteraction()
chrome_aut.test()
