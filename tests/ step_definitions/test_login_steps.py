import time

from pytest_bdd import scenarios, given, when, then, parsers
from pages.login_page import LoginPage

scenarios('../features/login.feature')


@given("I am on the login page")
def open_login_page(page, base_url):
    login = LoginPage(page)
    login.navigate(base_url)
    return login

@when("I enter valid username")
def enter_username(page, credentials):
    LoginPage(page).enter_username(credentials["username"])


@when("I enter valid password")
def enter_password(page, credentials):
    LoginPage(page).enter_password(credentials["password"])


@when("I click login")
def click_login(page):
    LoginPage(page).click_login()


@then("I should see the home page")
def verify_home_page(page):
    assert page.url.__contains__("https://rahulshettyacademy.com/loginpagePractise/")
    time.sleep(2)
@when(parsers.parse('I select the role as "{role}"'))
def click_login(page, role):
    LoginPage(page).select_role(role)

@when("I check the I Agree checkbox")
def click_login(page):
    LoginPage(page).check_box()