import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
  
  
def test_button_add_to_basket_on_page_item(browser):
    browser.get(link)
    button_add_to_basket = browser.find_elements(By.CLASS_NAME, "btn-add-to-basket")

    assert len(button_add_to_basket) > 0, "Button is not on page"

