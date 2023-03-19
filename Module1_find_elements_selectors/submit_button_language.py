from selenium import webdriver
from selenium.webdriver.common.by import By
import time 

link = 'https://www.google.com/'

try:
    browser = webdriver.Chrome()
    browser.get(link)
    button = browser.find_element(By.CSS_SELECTOR, '#SIvCob a[href^="https"]')
    button.click()

finally:
    time.sleep(10)
    browser.quit()
