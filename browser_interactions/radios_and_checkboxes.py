from selenium import webdriver
import os
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

class RadiosAndCheckboxes():

    def test(self):
        driver_location = 'C:\\Users\\BlazejW\\selenium\\chromedriver.exe'
        os.environ['webdriver.chrome.driver'] = driver_location
        driver = webdriver.Chrome(driver_location)
        driver.get("https://learn.letskodeit.com/p/practice")

        #RADIO ELEMENTS
        bmw_radio_element = driver.find_element_by_id("bmwradio")
        benz_radio_element = driver.find_element_by_id("benzradio")
        honda_radio_element = driver.find_element_by_id("hondaradio")
        #CHECKBOXES ELEMENTS
        bmw_check = driver.find_element_by_id("bmwcheck")
        benz_check = driver.find_element_by_id("benzcheck")
        honda_check = driver.find_element_by_id("hondacheck")

        bmw_radio_element.click()
        bmw_check.click()
        sleep(2)
        benz_radio_element.click()
        benz_check.click()
        sleep(3)
        bmw_radio_element.click()
        honda_check.click()
        sleep(3)
        honda_radio_element.click()
        sleep(3)

chrome_aut = RadiosAndCheckboxes()
chrome_aut.test()
