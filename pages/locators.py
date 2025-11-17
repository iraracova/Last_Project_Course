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
    FIELD_MESSAGE_ADDING = (By.CSS_SELECTOR, "div.alert:nth-child(1)")
    PRODUCT_TITLE = (By.CSS_SELECTOR, ".product_main > h1")
    PRODUCT_VALUE = (By.CSS_SELECTOR, ".product_main > p.price_color")
    BASKET_PRICE = (By.CSS_SELECTOR, ".alertinner p")

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link")
