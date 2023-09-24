from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.support.ui import WebDriverWait

class Page():
    def __init__(self, driver):
        
        self.driver = driver

        # The waiting time for check element located
        IMPLICIT_WAIT = 20
        self.driver.implicitly_wait(IMPLICIT_WAIT)

        # The waiting time for check element meet condition
        EXPLICIT_WAITS = 10
        self.explicit_wait = WebDriverWait(self.driver, EXPLICIT_WAITS)

        # The waiting time with frequency for check element meet condition
        FLUENT_WAITS = 10
        FLUENT_FREQUENCY = 2
        self.fluent_wait = WebDriverWait(self.driver, FLUENT_WAITS, 
                                         FLUENT_FREQUENCY)
        
    def open_browser(self, url):
        try:
            self.driver.get(url)
        except WebDriverException as e:
            print(f"Error: {e}")

    def close_browser(self):
        self.driver.quit()

    def maximum_window(self):
        self.driver.maximize_window()