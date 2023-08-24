from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link') #how and what


class LoginPageLocators():
    LOGIN_FORM = (By.ID, 'login_form')
    REGISTRATION_FORM = (By.ID, 'register_form')


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, '#login_link_inc')  
    BASKET_lINK = (By.CSS_SELECTOR, 'span a')


class BasketPageLocators():
    EMPTY_BASKET = (By.CSS_SELECTOR, '#content_inner p')


class ProductPageLocators():
    BUSKET_BUTTON = (By.CSS_SELECTOR, '.btn-add-to-basket')
    SUCCESS_MESSAGE = (By.CSS_SELECTOR,'.alert-success:nth-child(1)')
    PRODUCT_NAME = (By.CSS_SELECTOR, '.product_main h1')
    PRODUCT_NAME_IN_MESSAGE = (By.CSS_SELECTOR, '.alert-success:nth-child(1) div.alertinner strong')
    PRODUCT_PRICE = (By.CSS_SELECTOR, '.product_main .price_color')
    PRODUCT_PRICE_IN_MESSAGE = (By.CSS_SELECTOR, '.alert-info div.alertinner p strong')
   


