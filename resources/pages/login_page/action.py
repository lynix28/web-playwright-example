from playwright.sync_api import expect
from dotenv import load_dotenv
load_dotenv(".env")

import os, sys, re
sys.path.append(sys.path[0] + "/..")

from resources.pages.login_page.web_selectors import Selectors
selector = Selectors()

class Login:
    def __init__(self, page) -> None:
        self.page = page

    def go_to_web(self):
        self.page.goto(os.getenv("BASE_URL"), wait_until="networkidle")

    def check_content(self, pageTitle, loginText):
        self.page.wait_for_selector(selector.page_title(), state="visible", timeout=10000)
        self.page.wait_for_selector(selector.username_placeholder(), state="visible", timeout=10000)
        self.page.wait_for_selector(selector.password_placeholder(), state="visible", timeout=10000)
        self.page.wait_for_selector(selector.login_button(), state="visible", timeout=10000)

        expect(self.page).to_have_title(re.compile(pageTitle))
        expect(self.page.locator(selector.login_button())).to_have_text(re.compile(loginText))

    def fill_username(self, username):
        self.page.fill(selector.username_placeholder(), username)
    
    def fill_password(self, password):
        self.page.fill(selector.password_placeholder(), password)
        
    def click_login(self):
        self.page.click(selector.login_button())

    def check_error_message(self, errorText):
        self.page.wait_for_selector(selector.invalid_credential_info(), state="visible", timeout=10000)
        expect(self.page.locator(selector.invalid_credential_info())).to_have_text(re.compile(errorText))