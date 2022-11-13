from selenium import webdriver
from selenium.webdriver.common.by import By
import time 
from selenium.webdriver.common.action_chains import ActionChains

browser = webdriver.Chrome()
browser.get("https://opensea.io/collection/halloween-poupelle")

browser.execute_script("window.scrollBy(0, 600);")

action = ActionChains(browser)

firstElementHover = browser.find_element(By.XPATH, '//div[@class="sc-29427738-0 dVNeWL AssetsSearchView--assets"] //div[3][@class="sc-29427738-0 dVNeWL Asset--loaded"]')
action.move_to_element(firstElementHover).perform()
secondElementClick = browser.find_element(By.XPATH, '//div[@class="sc-29427738-0 dVNeWL AssetsSearchView--assets"] //div[3][@class="sc-29427738-0 dVNeWL Asset--loaded"]//button[@class="sc-29427738-0 sc-65824775-0 kqzAEQ gabBOa sc-4daa6fa8-0 bugqwW"]')
action.move_to_element(secondElementClick).perform()

secondElementClick.click()

goods = browser.find_elements(By.XPATH, '//*[@data-testid="shopping-cart"]//child::ul')

assert len(goods) == 1

time.sleep(3)
browser.quit()

