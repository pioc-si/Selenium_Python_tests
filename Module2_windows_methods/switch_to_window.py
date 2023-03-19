from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/redirect_accept.html"
browser = webdriver.Chrome()
browser.get(link)

magic_button = browser.find_element(By.CLASS_NAME, 'trollface').click()

browser.switch_to.window(browser.window_handles[1])

element = browser.find_element(By.ID, 'input_value')
x = element.text
y = calc(x)

answer_form = browser.find_element(By.ID, 'answer').send_keys(y)
submit_button = browser.find_element(By.CLASS_NAME, 'btn').click()

time.sleep(3)

browser.quit()


