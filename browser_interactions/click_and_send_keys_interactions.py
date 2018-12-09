from selenium import webdriver
import os
from time import sleep

class ClickAndSendKeys():

    def test(self):
        driver_location = 'C:\\Users\\BlazejW\\selenium\\chromedriver.exe'
        os.environ['webdriver.chrome.driver'] = driver_location
        driver = webdriver.Chrome(driver_location)
        driver.get("https://learn.letskodeit.com/p/practice")
        driver.maximize_window()

        #PAGE LINKS
        practice_link = driver.find_element_by_link_text("Practice")
        login_link = driver.find_element_by_link_text("Login")
        sign_up_link = driver.find_element_by_link_text("Sign Up")

        login_link.click()
        driver.implicitly_wait(6)

        #LOGIN PAGE ELEMENTS
        user_email_input = driver.find_element_by_id("user_email")
        user_password_input = driver.find_element_by_id("user_password")
        login_button = driver.find_element_by_name("commit")


        user_email_input.send_keys("test")
        user_password_input.send_keys("testtest")
        sleep(3)
        user_email_input.clear()
        user_password_input.clear()
        sleep(3)
        user_email_input.send_keys("TEST@test.com")
        user_password_input.send_keys("TESTTESTTEST")
        login_button.click()
        sleep(3)

chrome_aut =  ClickAndSendKeys()
chrome_aut.test()
