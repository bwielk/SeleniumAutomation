from selenium import webdriver
import os

class RunChromeTests():
    # http://chromedriver.storage.googleapis.com/index.html

    def test(self):
        driverLocation = 'C:\\Users\\BlazejW\\selenium\\chromedriver.exe'
        os.environ["webdriver.chrome.driver"] = driverLocation
        driver = webdriver.Chrome(driverLocation)
        driver.get("http://www.letskodeit.com")

ff = RunChromeTests()
ff.test()