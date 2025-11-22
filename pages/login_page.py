from pages.base_page import BasePage

class LoginPage(BasePage):

    def __init__(self, page):
        super().__init__(page)
        self.username_input = page.get_by_label("Username:")
        self.password_input = page.get_by_label("Password:")
        self.role_dropdown = page.get_by_role("combobox")
        self.term_checkbox = page.get_by_role("checkbox", name="terms and conditions")
        self.sign_in_button = page.get_by_role("button", name="Sign In")

    def enter_username(self, username):
        self.username_input.fill(username)

    def enter_password(self, password):
        self.password_input.fill(password)

    def click_login(self):
        self.sign_in_button.click()

    def select_role(self, role):
        self.role_dropdown.select_option(role)

    def check_box(self):
        self.term_checkbox.click()