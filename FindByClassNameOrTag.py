from selenium import webdriver
import os

class FindByLinkText():

    def test(self):
        driver_location = 'C:\\Users\\BlazejW\\selenium\\chromedriver.exe'
        os.environ['webdriver.chrome.driver'] = driver_location
        driver = webdriver.Chrome(driver_location)
        driver.get("https://learn.letskodeit.com/p/practice")
        element_by_class_name= driver.find_element_by_class_name("left-align")
        elements_by_tag_name = driver.find_elements_by_tag_name("li")
        elements_by_partial_class_name = driver.find_elements_by_class_name("inputs")

        if element_by_class_name or elements_by_tag_name is not None:
            print("Elements have been found")

        for element in elements_by_tag_name:
            print(element.text)

        printing_all_els = map(lambda x: x, elements_by_partial_class_name)
        print(list(printing_all_els))


chrome_aut = FindByLinkText()
chrome_aut.test()