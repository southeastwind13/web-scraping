from common import base_page
from common import base_action
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class GoogleElements():
    search_box_element = (By.XPATH, "//textarea[@name='q']")
    search_results_element = (By.XPATH, "//a[@jsname='UWckNb']/div/div//span[@class='VuuXrf']")
    reject_consent_button_element = (By.XPATH, "//button[@id='L2AGLb']")

class GoogleHomePage(base_page.BasePage, base_action.BaseAction):
    def open(self):
        url = 'https://www.google.com'
        self.open_browser(url)

    def close_consent(self):
        if(self.check_element_exist(*GoogleElements.reject_consent_button_element)):
           reject_button = self.find_element(*GoogleElements.reject_consent_button_element)
           reject_button.click()
        

    def search(self, search_term:str):
        search_box = self.find_element(*GoogleElements.search_box_element)
        self.wait_element_visible(search_box)
        search_box.send_keys(search_term)
        search_box.send_keys(Keys.ENTER)

    def get_search_results(self):
        title_search_results = self.find_elements(*GoogleElements.search_results_element)
        return title_search_results
