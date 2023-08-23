import pytest
from .pages.base_page import BasePage
from .pages.product_page import ProductPage
import time

def test_guest_can_add_product_to_basket(browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
        page = ProductPage(browser, link)
        page.open()
        page.add_product_to_basket()
        page.solve_quiz_and_get_code()
        page.should_be_success_message()
        time.sleep(8)
        #page.name_product_should_be_correct()
        #page.should_be_basket_price_message()
        #page.price_basket_and_price_product_should_be_correct()
