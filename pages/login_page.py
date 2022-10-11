from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "Expected login in url"

    def should_be_login_form(self):
        login_form = self.browser.find_element(LoginPageLocators.LOGIN_FORM)
        assert login_form, "Should be login form"

    def should_be_register_form(self):
        register_form = self.browser.find_element(LoginPageLocators.REGISTER_FORM)
        assert register_form, "Should be register form"
