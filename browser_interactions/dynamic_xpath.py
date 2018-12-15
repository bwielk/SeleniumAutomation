import time

from selenium import webdriver
import os

class DynamicXpath():

    def _prepare_driver(self):
        driver_location = 'C:\\Users\\BlazejW\\selenium\\chromedriver.exe'
        os.environ['webdriver.chrome.driver'] = driver_location
        driver = webdriver.Chrome(driver_location)
        driver.get('https://learn.letskodeit.com/')
        return driver

    def test(self):
        driver = self._prepare_driver()
        driver.find_element_by_partial_link_text('Login').click()
        driver.implicitly_wait(5)

        driver.find_element_by_id('user_email').send_keys('test@email.com')
        driver.find_element_by_id('user_password').send_keys('abcabc')
        driver.find_element_by_xpath('//*[@id="new_user"]/div[3]/input').click()

        driver.find_element_by_partial_link_text('All Courses').click()
        time.sleep(3)
        #driver.find_element_by_id('search-courses').send_keys('Java Script')

        #dynamic xpath
        _course = '//div[contains(@class, "course-listing-title")and contains(text(), "{0}")]'
        _course_locator = _course.format('JavaScript for beginners')

        element = driver.find_element_by_xpath(_course_locator)
        print(element)
        element.click()
        time.sleep(5)

chrome_aut = DynamicXpath()
chrome_aut.test()