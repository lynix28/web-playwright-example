# import re, os
# from playwright.sync_api import Page, expect
# from dotenv import load_dotenv

# load_dotenv()

# def test_case_001(page: Page):
#     page.set_viewport_size({
#         "width": 1680, 
#         "height": 844
#     })
#     page.goto(os.getenv("BASE_URL"))
#     expect(page).to_have_title(re.compile("Swag Labs"))
#     page.close()

# import sys
# sys.path.append(sys.path[0] + "/..")

# from playwright.sync_api import sync_playwright

# from resources.pages.login_page.action import Login
# from resources.shared.test_data import variables
# from resources.pages.login_page.test_asserts import validate

from playwright.sync_api import Playwright, sync_playwright, expect
import os, re
from dotenv import load_dotenv

load_dotenv()

def test(playwright: Playwright) -> None:
    browser_name = os.getenv("BROWSER")  # Get browser name from .env file
    browser = None

    if browser_name == "chromium":
        browser = playwright.chromium.launch(headless=False)
    elif browser_name == "firefox":
        browser = playwright.firefox.launch(headless=False)
    elif browser_name == "webkit":
        browser = playwright.webkit.launch(headless=False)
    else:
        raise ValueError("Invalid browser name")

    context = browser.new_context()
    page = context.new_page()

    page.goto("https://www.saucedemo.com/")
    page.wait_for_selector('text="Swag Labs"').click()
    page.fill('[data-test="username"]', "standard_user")
    page.fill('[data-test="password"]', "secret_sauce")
    page.click('[data-test="login-button"]')

    context.close()
    browser.close()

with sync_playwright() as playwright:
    test(playwright)
