from playwright.sync_api import Playwright

import sys, pytest
sys.path.append(sys.path[0] + "/..")

from resources.shared.test_setup import BrowserSingleton
from resources.pages.login_page.action import Login
from resources.pages.login_page.test_asserts import validate
from resources.shared.test_data import variables

@pytest.fixture(scope="session")
def setup(playwright: Playwright):
    setup = BrowserSingleton(playwright)
    yield setup.page
    setup.closeBrowser()

@pytest.mark.run(order=1)
def test_login(setup):
    login = Login(setup)
    login.goToWeb()
    login.checkContent(validate["PageTitle"], validate["LoginButtonText"])
    login.fillUsername(variables["username"])
    login.fillPassword(variables["password"])
    login.clickLogin()

@pytest.mark.run(order=2)
def test_login_invalidCredential(setup):
    login = Login(setup)
    login.goToWeb()
    login.checkContent(validate["PageTitle"], validate["LoginButtonText"])
    login.fillUsername(variables["invalid"]["username"])
    login.fillPassword(variables["invalid"]["password"])
    login.clickLogin()
    login.checkErrorMessage(validate["InvalidCredentialText"])