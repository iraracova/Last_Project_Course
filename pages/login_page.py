import pytest
from selenium import webdriver
from .locators import MainPageLocators
from .locators import LoginPageLocators
from .base_page import BasePage


class LoginPage(BasePage):
    def should_be_login_page(self):
        login_link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        login_link.click()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "login is not presented in current url"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "login form is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "register form is not presented"
