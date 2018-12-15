import time
from selenium import webdriver
import os
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

class Wrappers():

    def _prepare_driver(self):
        driver_location = 'C:\\Users\\BlazejW\\selenium\\chromedriver.exe'
        os.environ['webdriver.chrome.driver'] = driver_location
        driver = webdriver.Chrome(driver_location)
        driver.get('https://learn.letskodeit.com/p/practice')
        return driver

    def test(self):
        driver = self._prepare_driver()
        wrapper = HandyWrappers(driver)
        text_field_1 = wrapper.get_element('name')
        text_field_1.send_keys('Mein vorname ist Blazej. Ich komme aus Polen')
        time.sleep(4)
        text_field_2 = wrapper.get_element('//input[@id="name"]', locator_type='XPath')
        text_field_2.clear()
        text_field_2.send_keys('Ich koche gern')
        time.sleep(4)
        text_field_3 = wrapper.get_element('text-field', 'class') #should throw exception
        print(text_field_3)
        time.sleep(3)

class HandyWrappers():

    def __init__(self, driver):
        self.driver = driver

    def get_by_type(self, locator_type):
        locator_type = locator_type.lower()
        if locator_type == 'id':
            return By.ID
        elif locator_type == 'xpath':
            return By.XPATH
        else:
            raise ValueError('This locator is not supported')

    def get_element(self, locator, locator_type='id'):
        element = None
        try:
            locator_type = locator_type.lower()
            by_type = self.get_by_type(locator_type)
            element = self.driver.find_element(by_type, locator)
            print("Element found")
        except NoSuchElementException:
            print('Element not found')
        return element

chrome_aut = Wrappers()
chrome_aut.test()
