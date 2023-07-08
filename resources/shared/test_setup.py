from distutils.util import strtobool
from dotenv import load_dotenv
load_dotenv(".env")

import os

class Launch_Browser:
    def __init__(self, playwright) -> None:
        self.playwright = playwright

    def launchBrowser(self):
        browser_name = os.getenv("BROWSER")
        headless = bool(strtobool(os.getenv("HEADLESS")))
        self.browser = None

        if browser_name == "chromium":
            self.browser = self.playwright.chromium.launch(headless=headless)
        elif browser_name == "firefox":
            self.browser = self.playwright.firefox.launch(headless=headless)
        elif browser_name == "webkit":
            self.browser = self.playwright.webkit.launch(headless=headless)
        else:
            raise ValueError("Invalid browser name")

        self.context = self.browser.new_context()
        self.page = self.context.new_page()

        self.page.set_viewport_size({
            "width": 1680, 
            "height": 844
        })

    def closeBrowser(self):
        self.page.close()