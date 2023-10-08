# Set directory to be 2 steps above
import os,sys,inspect
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
parent_parent_dir = os.path.dirname(parent_dir)
sys.path.insert(0, parent_parent_dir) 


from common import browser_factory
from google.pages.home_page import GoogleHomePage

driver_path = "driver/chromedriver"
is_option = True
is_headless = False

web = browser_factory.Browser(driver_path, is_option, is_headless)

google_home_page = GoogleHomePage(web.driver)
google_home_page.open()
google_home_page.close_consent()
google_home_page.search("test search")
google_home_page.scroll_to_end()
google_home_page.get_titles_search_results()
google_home_page.close_browser()