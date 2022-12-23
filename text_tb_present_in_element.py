from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()

browser.get("http://suninjuly.github.io/explicit_wait2.html")

WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, 'price'), "100"))

book_button = browser.find_element(By.ID, 'book').click()

browser.execute_script("window.scrollBy(0, 100);")

element = browser.find_element(By.ID, 'input_value')
x = element.text
y = calc(x)

answer_form = browser.find_element(By.ID, 'answer').send_keys(y)

submit_button = browser.find_element(By.ID, 'solve').click()
