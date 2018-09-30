from selenium import webdriver
from time import sleep

driver = webdriver.Firefox()
url = 'https://localhost/iwebshop/'
driver.get(url)
driver.maximize_window()
driver.implicitly_wait(10)

sleep(3)
driver.quit()
