from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))


driver = webdriver.Firefox()

# Откройте страницу http://the-internet.herokuapp.com/entry_ad.

driver.get("http://the-internet.herokuapp.com/entry_ad")

# В модальном окне нажмите на кнопку Сlose
close_button = driver.find_element(By.CSS_SELECTOR, "div.modal-footer").click()

sleep(5)
