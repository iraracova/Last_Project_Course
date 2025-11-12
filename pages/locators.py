import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")

class ProductPageLocators():
    BUTTON_ADD_TO_BUSKET = (By.CSS_SELECTOR, "button.btn-add-to-basket")
    FIELD_MESSAGE_ADDING = (By.CSS_SELECTOR, "#messages")
    PRODUCT_TITLE = (By.TAG_NAME, "h1")
    PRODUCT_VALUE = (By.CSS_SELECTOR, "p.price_color")
