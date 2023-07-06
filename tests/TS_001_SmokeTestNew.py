from playwright.sync_api import sync_playwright

import sys
sys.path.append(sys.path[0] + "/..")

from resources.pages.login_page.action import Login
from resources.pages.login_page.test_asserts import validate
from resources.shared.test_data import variables

def testcase_login() -> None:
    with sync_playwright() as playwright:
        playwright = Login(playwright)
        playwright.launchWeb()
        playwright.checkContent(validate["PageTitle"], validate["LoginButtonText"])
        playwright.fillUsername(variables["username"])
        playwright.fillPassword(variables["password"])
        playwright.clickLogin()
        playwright.closeBrowser()