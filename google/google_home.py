from common import page

class GoogleHome(page.Page):
    def open(self):
        url = 'https://www.google.com'
        self.open_browser(url)