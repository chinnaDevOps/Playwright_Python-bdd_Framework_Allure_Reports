import time

from pytest_bdd import scenarios, given, when, then, parsers
from pages.login_page import LoginPage

scenarios('../features/login.feature')


@given("I am on the login page")
def open_login_page(page):
    login = LoginPage(page)
    login.navigate("https://rahulshettyacademy.com/loginpagePractise")
    return login

@when(parsers.parse('I enter username "{username}"'))
def enter_username(page, username):
    LoginPage(page).enter_username(username)

@when(parsers.parse('I enter password "{password}"'))
def enter_password(page, password):
    LoginPage(page).enter_password(password)

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