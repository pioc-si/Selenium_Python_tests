from selenium import webdriver
from selenium.webdriver.firefox.options import Options

options = Options()
options.binary_location = r'/usr/bin/firefox'
driver = webdriver.Firefox(executable_path=r'/usr/local/bin/geckodriver', options=options)
driver.get("https://stepik.org/lesson/25969/step/8")

