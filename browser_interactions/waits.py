from selenium import webdriver
import os
from time import sleep

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
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
        driver = self._prepare_driver('https://www.airbnb.co.uk/')
        driver.maximize_window()

        magic_carpet_search_bar = None

        try:
            magic_carpet_search_bar = driver.find_element(By.ID, 'MagicCarpetSearchBar')
        except NoSuchElementException:
            print('Element not found')

        if magic_carpet_search_bar is None:

            driver.implicitly_wait(5)

            destination_input = driver.find_element(By.XPATH, '//*[@id="Koan-guided-search-location__input"]')
            time_and_date = driver.find_element(By.XPATH, '//*[@id="guided-search-location"]/div/div[2]/div/div/div[1]/div/div[2]/div/div/div[2]/button/div')

            destination_input.send_keys('Warsaw')
            time_and_date.click()

            particular_date = driver.find_element(By.XPATH, '//*[@id="guided-search-location"]/div/div[2]/div/div/div[1]/div/div[2]/div/div[1]/div[2]/div/div/div/\
                            div/div/div[1]/div/div/div[2]/div[2]/div/div[2]/div/table/tbody/tr[2]/td[6]')
            particular_date.click()

            apply_time_and_date = driver.find_element(By.XPATH,
                                                      '//*[@id="guided-search-location"]/div/div[2]/div/div/div[1]/div/div[2]/div/div[1]/div[2]/div/div/div/div/div/div[2]/span/button')
            apply_time_and_date.click()

            guests_number = driver.find_element(By.XPATH,
                                                '//*[@id="guided-search-location"]/div/div[2]/div/div/div[1]/div/div[3]/div/div/div[2]/div/button')
            guests_number.click()

            add_an_adult_button = driver.find_element(By.XPATH,
                                                      '//*[@id="guided-search-location"]/div/div[2]/div/div/div[1]/div/div[3]/div/div/div[2]/div/div/div/div[1]/div[1]/div/div/div/div[2]/div/div[3]/button')

            add_an_adult_button.click()
            add_an_adult_button.click()
            search_button = driver.find_element(By.XPATH, '//*[@id="guided-search-location"]/div/div[2]/div/div/div[2]/button')
            search_button.click()
            sleep(60)
        else:
            driver.close()

chrome_aut = Waits()
#chrome_aut.implicit_waits()
chrome_aut.explicit_wait()
