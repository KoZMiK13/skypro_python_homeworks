from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))


driver = webdriver.Chrome()

#Откройте страницу http://uitestingplayground.com/classattr.

driver.get("http://uitestingplayground.com/classattr")

# Кликните на синюю кнопку. 
click_button = driver.find_element(By.XPATH, "//button[contains(concat(' ', normalize-space(@class), ' '), ' btn-primary ')]").click()

sleep(5)