from playwright.sync_api import Playwright, sync_playwright, expect
import os, re
from dotenv import load_dotenv
load_dotenv()

import sys
sys.path.append(sys.path[0] + "/..")

from resources.pages.login_page.web_selectors import Selectors
selector = Selectors()

from resources.pages.login_page.test_asserts import validate
from resources.shared.test_data import variables

def test(playwright: Playwright) -> None:
    browser_name = os.getenv("BROWSER")
    browser = None
    headless = False

    if browser_name == "chromium":
        browser = playwright.chromium.launch(headless=headless)
    elif browser_name == "firefox":
        browser = playwright.firefox.launch(headless=headless)
    elif browser_name == "webkit":
        browser = playwright.webkit.launch(headless=headless)
    else:
        raise ValueError("Invalid browser name")

    context = browser.new_context()
    page = context.new_page()

    page.set_viewport_size({
        "width": 1680, 
        "height": 844
    })
    page.goto(os.getenv("BASE_URL"), wait_until="networkidle")
    page.wait_for_selector(selector.pageTitle(), state="visible", timeout=10000)
    expect(page).to_have_title(re.compile(validate["PageTitle"]))
    page.wait_for_selector(selector.usernamePlaceholder(), state="visible", timeout=10000)
    page.fill(selector.usernamePlaceholder(), variables["username"])
    page.wait_for_selector(selector.passwordPlaceholder(), state="visible", timeout=10000)
    page.fill(selector.passwordPlaceholder(), variables["password"])
    page.wait_for_selector(selector.loginButton(), state="visible", timeout=10000)
    expect(page.locator(selector.loginButton())).to_have_text(validate["LoginButtonText"])
    page.click(selector.loginButton())

    context.close()
    browser.close()

with sync_playwright() as playwright:
    test(playwright)
