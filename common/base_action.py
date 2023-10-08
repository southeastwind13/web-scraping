from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.keys import Keys


class BaseAction():
    def __init__(self, driver):
        self.driver = driver

    def open_browser(self, url):
        try:
            self.driver.get(url)
        except WebDriverException as e:
            print(f"Error: {e}")

    def open_browser_hide_proxy(self, url):
        hideme_url = "https://hide.me/en/proxy"
        self.driver.get(hideme_url)

        text_url = self.find_element(*(By.XPATH, "//input[@id='u']"))
        text_url.send_keys(url)
        text_url.send_keys(Keys.ENTER)

    def maximum_window(self):
        self.driver.maximize_window()

    def close_browser(self):
        self.driver.quit()

    def close_tab(self):
        self.driver.close()

    def scroll_to_end(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")