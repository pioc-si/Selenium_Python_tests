from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_product_to_basket(self):
        add_to_basket_button = self.browser.find_element(*ProductPageLocators.BUSKET_BUTTON)
        add_to_basket_button.click()

    def should_be_success_message(self):
        assert self.is_element_present(*ProductPageLocators.SUCCESS_MESSAGE), 'There is no success message'


    #def name_added_product_should_be_correct(self):
     #   product_name = self.browser.find_element(*ProductPageLocators.BUSKET_BUTTON)



 

    

