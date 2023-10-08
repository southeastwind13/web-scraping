# Set directory to be 2 steps above
import os,sys,inspect
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
parent_parent_dir = os.path.dirname(parent_dir)
sys.path.insert(0, parent_parent_dir) 

from common import browser_factory
from herokuapp.pages.herokupapp_home import HerokuappHomePage

driver_path = "driver/chromedriver"
is_option = True
is_headless = False

web = browser_factory.Browser(driver_path, is_option, is_headless)

herokuapp_home_page = HerokuappHomePage(web.driver)
herokuapp_home_page.open()
herokuapp_home_page.open_add_remove_page()
herokuapp_home_page.close_browser()