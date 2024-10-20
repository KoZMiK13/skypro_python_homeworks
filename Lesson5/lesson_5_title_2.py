from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))


driver = webdriver.Chrome()

#Откройте страницу http://uitestingplayground.com/dynamicid.

driver.get("http://uitestingplayground.com/dynamicid")

# Кликните на синюю кнопку. <button class="btn btn-primary" type="button" id="93f4fb73-419e-fa4f-e943-030dc079fce4">Button with Dynamic ID</button>

click_button = driver.find_element(By.XPATH, '//button[text()="Button with Dynamic ID"]').click()

sleep(5)