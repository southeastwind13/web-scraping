from common import base_page
from common import base_action
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class HerokappElements():
    add_remove_link_element = (By.XPATH, "//a[text()='Add/Remove Elements']")

class HerokuappHomePage(base_page.BasePage, base_action.BaseAction):
    def open(self):
        url = 'https://the-internet.herokuapp.com/'
        self.open_browser(url)

    def open_add_remove_page(self):
        link_add_remove_page = self.find_element(*HerokappElements.add_remove_link_element)
        link_add_remove_page.click()

    