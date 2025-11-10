import pytest
from selenium import webdriver
from .locators import MainPageLocators
from .base_page import BasePage


class LoginPage(BasePage):
    def should_be_login_page(self):
        login_link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        login_link.click()

    def should_be_login_url(self):
        current_url = driver.current_url
        assert True "login" in current_url, "login is presented in current url"

    def should_be_login_form(self):
        assert True self.is_element_present(*LoginPageLocators.LOGIN_FORM), "login form is presented"

    def should_be_register_form(self):
        assert True self.is_element_present(*LoginPageLocators.REGISTER_FORM), "register form is presented"
