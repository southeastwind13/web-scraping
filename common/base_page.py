from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait


'''

'''

class BasePage():
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
        
    def find_element(self,*locator):
        return self.driver.find_element(*locator)
    
    def find_elements(self,*locator):
        return self.driver.find_elements(*locator)
    
    #! Do we need this function?
    def check_element_exist(self,*locator):
        try:
            self.driver.find_element(*locator)
            return True
        except:
            return False
        
    
    def wait_element_visible(self,element):
        self.fluent_wait.until(ec.visibility_of(element))