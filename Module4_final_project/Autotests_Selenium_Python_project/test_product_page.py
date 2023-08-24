import pytest
from .pages.base_page import BasePage
from .pages.product_page import ProductPage
import time

@pytest.mark.parametrize('number_link', [0, 1, 2, 3, 4, 5, 6,
                                 pytest.param(7, marks=pytest.mark.xfail),
                                 8, 9])
                
class TestClass:
        def test_guest_can_add_product_to_basket(self, browser, number_link):
                link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{number_link}"
                page = ProductPage(browser, link)
                page.open()
                page.add_product_to_basket()
                page.solve_quiz_and_get_code()
                page.should_be_success_message()
                print('test_guest_can_add_product_to_basket')
                #time.sleep(1000)
        
        def test_should_be_success_message(self, browser, number_link):
                link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{number_link}"
                page = ProductPage(browser, link)
                page.open()
                page.add_product_to_basket()
                page.solve_quiz_and_get_code()
                page.should_be_success_message()
                page.success_message_is_disappeared()
                print('test_should_be_success_message')
        
        @pytest.mark.xfail(reason="fixing this bug right now")
        def test_should_be_correct_name_product(self, browser, number_link):
                link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{number_link}"
                page = ProductPage(browser, link)
                page.open()
                page.add_product_to_basket()
                page.solve_quiz_and_get_code()
                page.should_be_success_message()
                page.should_be_correct_name_product()
                print('test_should_be_correct_name_product')


        def test_should_be_basket_price_message(self, browser, number_link):
                link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{number_link}"
                page = ProductPage(browser, link)
                page.open()
                page.add_product_to_basket()
                page.solve_quiz_and_get_code()
                page.should_be_success_message()
                page.should_be_basket_price_message()
                print('test_should_be_basket_price_message')


        def test_should_be_correct_price_product_in_message_and_price_product(self, browser, number_link):
                link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{number_link}"
                page = ProductPage(browser, link)
                page.open()
                page.add_product_to_basket()
                page.solve_quiz_and_get_code()
                page.should_be_success_message()
                page.should_be_basket_price_message()
                page.should_be_correct_price_product_in_message_and_price_product
                print('test_should_be_correct_price_product_in_message_and_price_product')

