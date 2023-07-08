from playwright.sync_api import Playwright

import sys, pytest
sys.path.append(sys.path[0] + "/..")

from resources.shared.test_setup import Launch_Browser
from resources.pages.login_page.action import Login
from resources.pages.login_page.test_asserts import validate
from resources.shared.test_data import variables

@pytest.fixture
def setup(playwright: Playwright):
    setup = Launch_Browser(playwright)
    setup.launchBrowser()
    yield setup.page
    setup.closeBrowser()

def test_login(setup):
    login = Login(setup)
    login.goToWeb()
    login.checkContent(validate["PageTitle"], validate["LoginButtonText"])
    login.fillUsername(variables["username"])
    login.fillPassword(variables["password"])
    login.clickLogin()