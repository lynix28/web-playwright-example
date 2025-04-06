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
    setup.close_browser()

@pytest.mark.run(order=1)
def test_login(setup):
    login = Login(setup)
    login.go_to_web()
    login.check_content(validate["PageTitle"], validate["LoginButtonText"])
    login.fill_username(variables["username"])
    login.fill_password(variables["password"])
    login.click_login()

@pytest.mark.run(order=2)
def test_login_invalid_credential(setup):
    login = Login(setup)
    login.go_to_web()
    login.check_content(validate["PageTitle"], validate["LoginButtonText"])
    login.fill_username(variables["invalid"]["username"])
    login.fill_password(variables["invalid"]["password"])
    login.click_login()
    login.check_error_message(validate["InvalidCredentialText"])