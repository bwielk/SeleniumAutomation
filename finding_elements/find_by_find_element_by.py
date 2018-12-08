from selenium import webdriver
from selenium.webdriver.common.by import By
import os

class FindByFindElementBy():

    def test(self):
        driver_location = 'C:\\Users\\BlazejW\\selenium\\chromedriver.exe'
        os.environ['webdriver.chrome.driver'] = driver_location
        driver = webdriver.Chrome(driver_location)
        driver.get("https://learn.letskodeit.com/p/practice")

        dictionary_of_elements = {}
        dictionary_of_elements["elements_retrieved_by_id"] = driver.find_elements(By.ID, "openwindow")
        dictionary_of_elements["elements_retrieved_by_fieldset_tag"] = driver.find_elements(By.TAG_NAME, "fieldset")
        dictionary_of_elements["elements_retrieved_by_link_text"] = driver.find_elements(By.LINK_TEXT, "Sign Up")
        dictionary_of_elements["elements_retrieved_by_xpath"] = driver.find_elements(By.XPATH, "//*[@id='block-1069048']")
        dictionary_of_elements["elements_retrieved_by_name"] = driver.find_elements(By.NAME, "cars")

        for k,v in dictionary_of_elements.items():
            print(k, "=>", len(v))


chrome_aut = FindByFindElementBy()
chrome_aut.test()