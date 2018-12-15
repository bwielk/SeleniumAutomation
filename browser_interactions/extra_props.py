from selenium import webdriver
import os

class ExtraProperties():

    def _prepare_driver(self):
        driver_location = 'C:\\Users\\BlazejW\\selenium\\chromedriver.exe'
        os.environ['webdriver.chrome.driver'] = driver_location
        driver = webdriver.Chrome(driver_location)
        driver.get('https://learn.letskodeit.com/p/practice')
        return driver

    def get_text(self):
        driver = self._prepare_driver()
        open_tab_element = driver.find_element_by_id('opentab')
        open_tab_element_text = open_tab_element.text
        print('text on element is %s' % open_tab_element_text)



chrome_aut = ExtraProperties()
chrome_aut.get_text()


