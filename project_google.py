from common import browser_factory
from google.google_home import GoogleHome

driver_path = "driver/chromedriver"
is_option = True
is_headless = False

web = browser_factory.Browser(driver_path, is_option, is_headless)

google_home = GoogleHome(web.driver)
google_home.open()
google_home.close_browser()