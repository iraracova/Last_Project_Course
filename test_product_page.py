import pytest
from selenium import webdriver
import time
from .pages.product_page import ProductPage
from .pages.base_page import BasePage

def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, link)
    page.open()
    time.sleep(20)
    page.add_product_to_basket()
    get_code = BasePage(browser, link)
    get_code.solve_quiz_and_get_code()
    page.checking_addition_of_product()
    page.checking_busket_value()
