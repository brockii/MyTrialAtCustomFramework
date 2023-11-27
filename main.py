from selenium import webdriver
import time

class Browser:
    def __init__(self, browser_name, url):
        self.resolution = (1920, 1080)
        self.driver = None
        if browser_name.lower() == "chrome":
            self.driver = webdriver.Chrome()
            self.driver.maximize_window()
            self.driver.get(url)

        elif browser_name.lower() == "edge":
            self.driver = webdriver.Edge()
            self.driver.get(url)

        else:
            raise ValueError("The value provided is not cool")

    def wait(self, time_duration):
        time.sleep(time_duration)


    def click_on_element(self, element):
        element = self.find(element)    #self makes sure that the current instance opened is the one using the right function
        element.click()

    def find(self, identifier):
        element = self.driver.find_element(by="xpath", value=identifier)
        return element
