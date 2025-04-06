from dotenv import load_dotenv
from playwright.sync_api import expect

load_dotenv(".env")

import sys, re
sys.path.append(sys.path[0] + "/..")

from resources.pages.dashboard.web_selectors import Selectors
selector = Selectors()

class Dashboard:
    def __init__(self, page) -> None:
        self.page = page

    def check_content(self, header_title_text, header_content_title_text):
        self.page.wait_for_selector(selector.header_title(), state="visible", timeout=10000)
        self.page.wait_for_selector(selector.header_side_menu_button(), state="visible", timeout=10000)
        self.page.wait_for_selector(selector.header_shopping_cart_button(), state="visible", timeout=10000)
        # self.page.wait_for_selector(selector.header_sort_button(), state="visible", timeout=10000)
        self.page.wait_for_selector(selector.header_content_title(), state="visible", timeout=10000)
        self.page.wait_for_selector(selector.body_content_container(), state="visible", timeout=10000)

        expect(self.page.locator(selector.header_title())).to_have_text(re.compile(header_title_text))
        expect(self.page.locator(selector.header_content_title())).to_have_text(re.compile(header_content_title_text))

    def click_sidemenu(self):
        self.page.click(selector.header_side_menu_button())