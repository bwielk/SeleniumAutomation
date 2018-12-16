from selenium import webdriver
import os
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *

class Waits():

    def _prepare_driver(self, url):
        driver_location = 'C:\\Users\\BlazejW\\selenium\\chromedriver.exe'
        os.environ['webdriver.chrome.driver'] = driver_location
        driver = webdriver.Chrome(driver_location)
        driver.get(url)
        return driver

    def implicit_waits(self):
        driver = self._prepare_driver('https://learn.letskodeit.com/')
        driver.maximize_window()
        login_link = driver.find_element_by_xpath('//*[@id="navbar"]/div/div/div/ul/li[2]/a')
        login_link.click()

        driver.implicitly_wait(10)

        user_email_input = driver.find_element_by_id("user_email")
        user_email_input.send_keys('test')

    def explicit_wait(self):
        driver = self._prepare_driver('https://www.expedia.com')
        driver.find_element_by_id('package-origin-hp-package').send_keys("Warsaw")
        driver.find_element_by_id('package-destination-hp-package').send_keys("New York")
        driver.find_element_by_id('package-departing-hp-package').send_keys("24/12/2018")
        driver.find_element_by_id('package-returning-hp-package').clear()
        driver.find_element_by_id('package-returning-hp-package').send_keys("31/12/2018")
        driver.find_element_by_id('search-button-hp-package').click()

        driver.find_element_by_xpath('//*[@id="sortContainer"]/div/button').click()
        sleep(8)
        driver.quit()


chrome_aut = Waits()
#chrome_aut.implicit_waits()
chrome_aut.explicit_wait()
