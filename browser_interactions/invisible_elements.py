from selenium import webdriver
import os

class InvisibleElements():

    def test_lets_kode_it(self):
        driver_location = 'C:\\Users\\BlazejW\\selenium\\chromedriver.exe'
        os.environ['webdriver.chrome.driver'] = driver_location
        driver = webdriver.Chrome(driver_location)
        driver.get("https://learn.letskodeit.com/p/practice")
        driver.maximize_window()

        text_box_element = driver.find_element_by_id('displayed-text')
        show_button = driver.find_element_by_id('show-textbox')
        hide_button = driver.find_element_by_id('hide-textbox')

        show_button.click()
        driver.implicitly_wait(5)
        self._click_visible_or_invisible_lets_kode_it(text_box_element, hide_button, show_button)

        hide_button.click()
        driver.implicitly_wait(5)
        self._click_visible_or_invisible_lets_kode_it(text_box_element, hide_button, show_button)


    def _click_visible_or_invisible_lets_kode_it(self, text_box_element, hide_button, show_button):
        if text_box_element.is_displayed():
            hide_button.click()
        else:
            show_button.click()

    def test_expedia(self):
        driver_location = 'C:\\Users\\BlazejW\\selenium\\chromedriver.exe'
        os.environ['webdriver.chrome.driver'] = driver_location
        driver = webdriver.Chrome(driver_location)
        driver.get("https://www.expedia.co.uk/")
        driver.maximize_window()

        baby_age_dropdown = driver.find_element_by_id('package-1-age-select-1-hp-package')
        #baby_age_dropdown.click() Element not visible exception
        print("The baby aga dropdown is visible = " + str(baby_age_dropdown.is_displayed()))
        print(baby_age_dropdown.is_displayed())

chrome_aut = InvisibleElements()
chrome_aut.test_lets_kode_it()
chrome_aut.test_expedia()
