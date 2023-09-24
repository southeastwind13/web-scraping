from fake_useragent import UserAgent
from selenium import webdriver
from selenium.webdriver.chrome.service import Service



class Browser():
    def __init__(self, driver_path, is_option:bool = True, 
                 is_headless:bool = False):
        

        service = Service(executable_path=r'' + driver_path)
        self.options = webdriver.ChromeOptions()

        user_agent = UserAgent() #verify_ssl=False

        if(is_option):
            self.options.add_argument('--incognito')
            self.options.add_argument('disable-notifications')
            self.options.add_argument('--disable-infobars')
            self.options.add_argument('start-maximized')
            self.options.add_argument('disable-infobars')
            self.options.add_argument(f'user-agent={user_agent.random}')
            self.options.add_argument('--disable-gpu') #Why it necessary?

        if(is_headless == True):
            self.options.add_argument('--headless')

        self.driver = webdriver.Chrome(service=service,options = self.options)

    def get_driver(self):
        return self.driver