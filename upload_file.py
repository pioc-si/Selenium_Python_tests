from selenium import webdriver
from selenium.webdriver.common.by import By
import os

link = "http://suninjuly.github.io/file_input.html"
browser = webdriver.Chrome()
browser.get(link)

First_Name = browser.find_element(By.NAME, 'firstname')
First_Name.send_keys("Iva")
Last_Name = browser.find_element(By.NAME, 'lastname')
Last_Name.send_keys('Kli')
Email = browser.find_element(By.NAME, 'email')
Email.send_keys('k@mail.se')

current_dir = os.path.abspath(os.path.dirname('/home/pioc/environments/'))
file_path = os.path.join(current_dir, 'file_example.txt')
element = browser.find_element(By.NAME, 'file').send_keys(file_path)

button = browser.find_element(By.CLASS_NAME, 'btn')
button.click()

