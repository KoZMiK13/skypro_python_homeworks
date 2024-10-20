from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))


driver = webdriver.Firefox()

# Откройте страницу http://the-internet.herokuapp.com/login.

driver.get("http://the-internet.herokuapp.com/login")

# В поле username введите значение tomsmith.

input_username = driver.find_element(By.ID, "username")
input_username.send_keys("tomsmith")

# В поле password введите значение SuperSecretPassword! .

input_password = driver.find_element(By.ID, "password")
input_password.send_keys("SuperSecretPassword!")
sleep(5)

#Нажмите кнопку Login .<i class="fa fa-2x fa-sign-in"> Login</i>

click_login = driver.find_element(By.TAG_NAME, "button").click()

sleep(5)
