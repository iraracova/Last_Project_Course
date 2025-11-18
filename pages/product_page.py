import pytest
from selenium import webdriver
from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def add_product_to_basket(self):
        button_add_to_busket = self.browser.find_element(*ProductPageLocators.BUTTON_ADD_TO_BUSKET)
        button_add_to_busket.click()

    def checking_addition_of_product(self):
        field_message_adding = self.browser.find_element(*ProductPageLocators.FIELD_MESSAGE_ADDING)
        message_adding = field_message_adding.text
        product_title = self.browser.find_element(*ProductPageLocators.PRODUCT_TITLE).text
        assert f"{product_title} has been added to your basket" in message_adding, "The product has not been added to the cart"

    def checking_busket_value(self):
        field_message_adding = self.browser.find_element(*ProductPageLocators.FIELD_MESSAGE_ADDING)
        basket_price = self.browser.find_element(*ProductPageLocators.BASKET_PRICE).text
        product_value = self.browser.find_element(*ProductPageLocators.PRODUCT_VALUE).text
        assert f"Your basket total is now {product_value}" in basket_price, "The cart price does not match the product price"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.FIELD_MESSAGE_ADDING), \
            "Success message is presented, but should not be"

    def success_massage_should_be_disappear(self):
        assert self.is_disappeared(*ProductPageLocators.FIELD_MESSAGE_ADDING), \
               "Success message is presents, but should not be"

