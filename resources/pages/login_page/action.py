from playwright.sync_api import Page
from dotenv import load_dotenv
import os

load_dotenv(".env")

from resources.pages.login_page.web_selectors import Selectors

class Login:
    def __init__(self, page: Page) -> None:
        self.page = page

    def launchWeb(self):
        self.page.set_viewport_size({
            "width": 1680, 
            "height": 844
        })
        self.page.goto(os.getenv("BASE_URL"))

    def checkContent(self, data):
        self.page.locator(Selectors.pageTitle()).text_content(data)

    def fillUsername(self, data):
        self.page.locator(Selectors.usernamePlaceholder()).fill(data)
    
    def fillPassword(self, data):
        self.page.locator(Selectors.passwordPlaceholder()).fill(data)
        
    def clickLogin(self):
        self.page.locator(Selectors.loginButton()).click()

    def closeBrowser(self):
        self.page.close()
