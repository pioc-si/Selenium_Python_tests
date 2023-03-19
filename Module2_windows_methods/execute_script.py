from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "https://SunInJuly.github.io/execute_script.html"
browser = webdriver.Chrome()
browser.get(link)

element = browser.find_element(By.ID, 'input_value')
x = element.text
y = calc(x)

answer_form = browser.find_element(By.ID, 'answer').send_keys(y)

browser.execute_script("window.scrollBy(0, 50);")

checkbox = browser.find_element(By.CSS_SELECTOR, "[for='robotCheckbox']").click()
radiobutton = browser.find_element(By.CSS_SELECTOR, "[for='robotsRule']").click()

button = browser.find_element(By.CSS_SELECTOR, '.btn')
browser.execute_script("return arguments[0].scrollIntoView(true);", button)
button.click()

time.sleep(6)
browser.quit()





