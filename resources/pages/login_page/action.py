from playwright.sync_api import expect
from dotenv import load_dotenv
load_dotenv(".env")

import os, sys, re
sys.path.append(sys.path[0] + "/..")

from resources.pages.login_page.web_selectors import Selectors
selector = Selectors()

class Login:
    def __init__(self, playwright) -> None:
        browser_name = os.getenv("BROWSER")
        self.browser = None
        headless = False

        if browser_name == "chromium":
            self.browser = playwright.chromium.launch(headless=headless)
        elif browser_name == "firefox":
            self.browser = playwright.firefox.launch(headless=headless)
        elif browser_name == "webkit":
            self.browser = playwright.webkit.launch(headless=headless)
        else:
            raise ValueError("Invalid browser name")

        self.context = self.browser.new_context()
        self.page = self.context.new_page()

        self.page.set_viewport_size({
            "width": 1680, 
            "height": 844
        })

    def launchWeb(self):
        self.page.goto(os.getenv("BASE_URL"), wait_until="networkidle")

    def checkContent(self, pageTitle, loginText):
        self.page.wait_for_selector(selector.pageTitle(), state="visible", timeout=10000)
        self.page.wait_for_selector(selector.usernamePlaceholder(), state="visible", timeout=10000)
        self.page.wait_for_selector(selector.passwordPlaceholder(), state="visible", timeout=10000)
        self.page.wait_for_selector(selector.loginButton(), state="visible", timeout=10000)

        expect(self.page).to_have_title(re.compile(pageTitle))
        expect(self.page.locator(selector.loginButton())).to_have_text(loginText)

    def fillUsername(self, username):
        self.page.fill(selector.usernamePlaceholder(), username)
    
    def fillPassword(self, password):
        self.page.fill(selector.passwordPlaceholder(), password)
        
    def clickLogin(self):
        self.page.click(selector.loginButton())

    def closeBrowser(self):
        self.page.close()
