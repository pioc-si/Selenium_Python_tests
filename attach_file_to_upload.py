from selenium import webdriver
from selenium.webdriver.common.by import By
import time 

link = "http://suninjuly.github.io/file_input.html"
browser = webdriver.Chrome()
browser.get(link)

FirstName = browser.find_element(By.NAME, 'firstname')
FirstName.send_keys("Ivan")
LastName = browser.find_element(By.NAME, 'lastname')
LastName.send_keys("Petrov")
Email = browser.find_element(By.NAME, 'email')
Email.send_keys("cat@mail.com")

with open("FileToUpload.txt", "w") as file:
    content = file.write("shortbio") 

button = browser.find_element(By.CSS_SELECTOR, "button.btn")
button.click()

time.sleep(5)
browser.quit()