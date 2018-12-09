from selenium import webdriver
import os
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

class RadiosAndCheckboxes():

    is_selected_checker_counter = 0

    def _check_statues_of_checkboxes_and_radios(self, array_of_elements):
        self.is_selected_checker_counter += 1
        print("\n\nCHECKING SESSION NUMBER %s" % self.is_selected_checker_counter)
        for element in array_of_elements:
            print("%s is selected => %s" % (element.get_attribute("id"), element.is_selected()))

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

        #ARRAY OF ALL ELEMENTS
        all_selectable_elements = [bmw_radio_element, benz_radio_element, honda_radio_element, honda_check, benz_check, bmw_check]

        bmw_radio_element.click()
        bmw_check.click()
        self._check_statues_of_checkboxes_and_radios(all_selectable_elements)
        sleep(2)
        benz_radio_element.click()
        benz_check.click()
        self._check_statues_of_checkboxes_and_radios(all_selectable_elements)
        sleep(3)
        bmw_radio_element.click()
        honda_check.click()
        self._check_statues_of_checkboxes_and_radios(all_selectable_elements)
        sleep(3)
        honda_radio_element.click()
        self._check_statues_of_checkboxes_and_radios(all_selectable_elements)
        sleep(3)
        self.is_selected_checker_counter = 0

chrome_aut = RadiosAndCheckboxes()
chrome_aut.test()
