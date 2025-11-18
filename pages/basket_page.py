import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):
   def сhecking_that_no_products_in_basket(self):
       assert self.is_not_element_present(*BasketPageLocators.PRODUCT_ROW), \
            "Basket is not empty"

   def checking_that_message_about_empty_basket_is_present(self):
       assert self.is_element_present(*BasketPageLocators.MESSAGE_THAT_BASKET_IS_EMPTY), \
            "Message about empty basket is not present"
