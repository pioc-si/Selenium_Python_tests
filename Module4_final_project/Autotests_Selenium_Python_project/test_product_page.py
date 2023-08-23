import pytest
from .pages.base_page import BasePage
from .pages.product_page import ProductPage
import time

@pytest.mark.parametrize('offer_number', ["0","1", "3", "4", "5", "6", "7", "8", "9"])


def test_guest_can_add_product_to_basket(browser, offer_number):
        link = f'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{offer_number}'
        page = ProductPage(browser, link)
        page.open()
        page.add_product_to_basket()
        page.solve_quiz_and_get_code()
        page.should_be_success_message()
        print('test_guest_can_add_product_to_basket')

def test_should_be_success_message(browser, offer_number):
        link = f'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{offer_number}'
        page = ProductPage(browser, link)
        page.open()
        page.add_product_to_basket()
        page.solve_quiz_and_get_code()
        page.should_be_success_message()
        print('test_should_be_success_message')


def test_should_be_correct_name_product(browser, offer_number):
        link = f'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{offer_number}'
        page = ProductPage(browser, link)
        page.open()
        page.add_product_to_basket()
        page.solve_quiz_and_get_code()
        page.should_be_success_message()
        page.should_be_correct_name_product()
        print('test_should_be_correct_name_product')


def test_should_be_basket_price_message(browser, offer_number):
        link = f'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{offer_number}'
        page = ProductPage(browser, link)
        page.open()
        page.add_product_to_basket()
        page.solve_quiz_and_get_code()
        page.should_be_success_message()
        page.should_be_basket_price_message()
        print('test_should_be_basket_price_message')


def test_should_be_correct_price_product_in_message_and_price_product(browser, offer_number):
        link = f'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{offer_number}'
        page = ProductPage(browser, link)
        page.open()
        page.add_product_to_basket()
        page.solve_quiz_and_get_code()
        page.should_be_success_message()
        page.should_be_basket_price_message()
        page.should_be_correct_price_product_in_message_and_price_product
        print('test_should_be_correct_price_product_in_message_and_price_product')
