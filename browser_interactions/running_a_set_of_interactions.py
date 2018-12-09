from selenium import webdriver
import os
from time import sleep

class BrowserInteractions():

    browsing_history = []

    def _get_page_and_update_history(self, page_url, driver):
        driver.get(page_url)
        self.browsing_history.append({"url": page_url, "page_title": driver.title})

    def test(self):
        driver_location = 'C:\\Users\\BlazejW\\selenium\\chromedriver.exe'
        os.environ['webdriver.chrome.driver'] = driver_location
        driver = webdriver.Chrome(driver_location)
        self._get_page_and_update_history("https://learn.letskodeit.com/p/practice", driver)
        driver.maximize_window()
        driver.refresh()
        self._get_page_and_update_history("https://bbc.co.uk", driver)
        driver.get(driver.current_url)
        self._get_page_and_update_history("https://facebook.com", driver)
        driver.back()
        driver.forward()
        driver.back()
        driver.quit()
        print(self.browsing_history)


chrome_aut = BrowserInteractions()
chrome_aut.test()
