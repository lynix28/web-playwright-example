from distutils.util import strtobool
from dotenv import load_dotenv

import os
from resources.shared.test_data import variables
from resources.pages.login_page.web_selectors import Selectors

load_dotenv(".env")
selector = Selectors()


class BrowserSingleton:
    _instance = None

    def __new__(cls, playwright):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.playwright = playwright
            cls._instance.launchBrowser()
        return cls._instance

    def launchBrowser(self):
        browser_name = os.getenv("BROWSER")
        headless = bool(strtobool(os.getenv("HEADLESS")))
        width = int(os.getenv("WIDTH"))
        height = int(os.getenv("HEIGHT"))
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
            "width": width, 
            "height": height
        })

    def login(self):
        self.page.goto(os.getenv("BASE_URL"), wait_until="networkidle")

        self.page.wait_for_selector(selector.usernamePlaceholder(), state="visible", timeout=10000)
        self.page.fill(selector.usernamePlaceholder(), variables["username"])

        self.page.wait_for_selector(selector.passwordPlaceholder(), state="visible", timeout=10000)
        self.page.fill(selector.passwordPlaceholder(), variables["password"])

        self.page.wait_for_selector(selector.loginButton(), state="visible", timeout=10000)
        self.page.click(selector.loginButton())

    def closeBrowser(self):
        self.page.close()