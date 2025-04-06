from playwright.sync_api import Playwright
from pytest_bdd import scenarios, given, when, then, parsers

import sys, pytest
sys.path.append(sys.path[0] + "/..")

from resources.shared.test_setup import BrowserSingleton
from resources.pages.login_page.action import Login
from resources.pages.dashboard.action import Dashboard
from resources.pages.login_page.test_asserts import validate as login_validate
from resources.pages.dashboard.test_asserts import validate as dashboard_validate
from resources.shared.test_data import variables

scenarios("../features/login.feature")

@pytest.fixture(scope="session")
def setup(playwright: Playwright):
    setup = BrowserSingleton(playwright)
    yield setup.page
    setup.close_browser()

@given("Sauce Demo login page")
def login_page(setup):
    login = Login(setup)
    login.go_to_web()
    login.check_content(loginText=login_validate["LoginButtonText"], pageTitle=login_validate["PageTitle"])

@when("I enter a valid username")
def enter_valid_username(setup):
    login = Login(setup)
    login.fill_username(variables["username"])

@when("I enter an invalid username")
def enter_invalid_username(setup):
    login = Login(setup)
    login.fill_username(variables["invalid"]["username"])

@when(parsers.parse('I enter "{phrase}" as username'))
def enter_blocked_username(setup, phrase):
    login = Login(setup)
    login.fill_username(phrase)

@when("with a valid password")
def enter_valid_password(setup):
    login = Login(setup)
    login.fill_password(variables["password"])
    login.click_login()

@when("with an invalid password")
def enter_invalid_password(setup):
    login = Login(setup)
    login.fill_password(variables["invalid"]["password"])
    login.click_login()

@then("I can logged in and access the account")
def success_logged_in(setup):
    dashboard = Dashboard(setup)
    dashboard.check_content(header_title_text=dashboard_validate["page_header"]["title"], header_content_title_text=dashboard_validate["page_header"]["content_title"])

@then("I will see an error message")
def failed_logged_in_invalid_credential(setup):
    login = Login(setup)
    login.check_error_message(errorText=login_validate["InvalidCredentialText"])

@then("I will see an error message about the blocked credential")
def failed_logged_in_blocked_credential(setup):
    login = Login(setup)
    login.check_error_message(errorText=login_validate["BlockedCredentialText"])