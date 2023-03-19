from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "https://suninjuly.github.io/math.html"
browser = webdriver.Chrome()
browser.get(link)

x_element = browser.find_element(By.ID, 'input_value')
x = x_element.text
y = calc(x)

answer_form = browser.find_element(By.ID, 'answer').send_keys(y)

checkbox = browser.find_element(By.CSS_SELECTOR, "[for='robotCheckbox']").click()
radiobutton = browser.find_element(By.CSS_SELECTOR, "[for='robotsRule']").click()
button = browser.find_element(By.CSS_SELECTOR, '.btn').click()

time.sleep(5)
browser.quit()

