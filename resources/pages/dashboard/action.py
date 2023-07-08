from playwright.sync_api import expect
from dotenv import load_dotenv
load_dotenv("./env")

import sys, re
sys.path.append(sys.path[0] + "/..")

from resources.pages.dashboard.web_selectors import Selectors
selector = Selectors()

class Dashboard:
    def __init__(self, page) -> None:
        self.page = page

    def checkContent(self, headerTitleText, headerContentTitleText):
        self.page.wait_for_selector(selector.headerTitle(), state="visible", timeout=10000)
        self.page.wait_for_selector(selector.headerSideMenuButton(), state="visible", timeout=10000)
        self.page.wait_for_selector(selector.headerShoppingCartButton(), state="visible", timeout=10000)
        self.page.wait_for_selector(selector.headerSortButton(), state="visible", timeout=10000)
        self.page.wait_for_selector(selector.headerContentTitle(), state="visible", timeout=10000)
        self.page.wait_for_selector(selector.bodyContentContainer(), state="visible", timeout=10000)

        expect(self.page.locator(selector.headerTitle())).to_have_text(re.compile(headerTitleText))
        expect(self.page.locator(selector.headerContentTitle())).to_have_text(re.compile(headerContentTitleText))

    def clickSidemenu(self):
        self.page.click(selector.headerSideMenuButton())