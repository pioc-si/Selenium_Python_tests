from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import math

def sum(x, y):
  return str(x + y)

link = "https://suninjuly.github.io/selects1.html"
browser = webdriver.Chrome()
browser.get(link)

num1 = browser.find_element(By.ID, 'num1')
x = int(num1.text)

num2 = browser.find_element(By.ID, 'num2')
y = int(num2.text)

select = Select(browser.find_element(By.CLASS_NAME, "custom-select"))
select.select_by_value(sum(x,y))

button = browser.find_element(By.CSS_SELECTOR, '.btn').click()

time.sleep(8)
browser.quit()