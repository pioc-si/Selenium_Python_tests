from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "http://suninjuly.github.io/math.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

#check the people_radio value attribute checked 
    people_radio = browser.find_element(By.ID, 'peopleRule')
    people_checked = people_radio.get_attribute('checked')
    print('value of people radio: ', people_checked)
    assert people_checked is not None, "People radio is not selected by default"

#check the robots_radio value attribute checked 
    robots_radio = browser.find_element(By.ID, 'robotsRule')
    robots_checked = robots_radio.get_attribute('checked')
    print('value of robots_radio: ', robots_checked)
    assert robots_checked is None

#check the Submit button value attribute disabled
    button = browser.find_element(By.CSS_SELECTOR, '.btn')
    button_disabled = button.get_attribute('disabled')
    print('value of button Submit: ', button_disabled)
    assert button_disabled is None

#check the Submit button value attribute disabled after timeout
    time.sleep(5)
    button_disabled = button.get_attribute('disabled')
    print('value of button Submit after 10sec: ', button_disabled)
    assert button_disabled is not None

finally:
    browser.quit()

