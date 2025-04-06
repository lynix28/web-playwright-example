from playwright.sync_api import Playwright

import sys, pytest
sys.path.append(sys.path[0] + "/..")

from resources.shared.test_setup import BrowserSingleton
from resources.pages.dashboard.action  import Dashboard
from resources.pages.dashboard.test_asserts import validate

@pytest.fixture(scope="session")
def setup(playwright: Playwright):
    setup = BrowserSingleton(playwright)
    setup.login()
    yield setup.page
    setup.close_browser()

@pytest.mark.run(order=1)
def test_dashboard(setup):
    dashboard = Dashboard(setup)
    dashboard.check_content(validate["page_header"]["title"], validate["page_header"]["content_title"])
    dashboard.click_sidemenu()